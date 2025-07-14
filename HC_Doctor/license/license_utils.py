import os
import uuid
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib
import wmi
from datetime import datetime

LICENSE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'license.lic')
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'config.json')

# AES encryption key (should be kept secret and consistent)
# For demo purposes, using a fixed key derived from a passphrase
SECRET_KEY = hashlib.sha256(b"HarshComputronicsSecretKey2024").digest()

def get_hardware_id():
    """
    Generate hardware ID by combining MAC address and BIOS UUID
    """
    c = wmi.WMI()
    mac = None
    bios_uuid = None
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        mac = interface.MACAddress
        if mac:
            break
    for bios in c.Win32_BIOS():
        bios_uuid = bios.SerialNumber.strip()
        break
    if not mac:
        mac = "00:00:00:00:00:00"
    if not bios_uuid:
        bios_uuid = "UNKNOWNBIOSUUID"
    hwid = mac + bios_uuid
    return hwid

def encrypt_license_data(data: dict) -> str:
    """
    Encrypt license data dict to base64 string using AES
    """
    raw = json.dumps(data).encode('utf-8')
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(raw, AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return json.dumps({'iv': iv, 'ciphertext': ct})

def decrypt_license_data(enc_data: str) -> dict:
    """
    Decrypt license data from base64 string to dict
    """
    try:
        b64 = json.loads(enc_data)
        iv = base64.b64decode(b64['iv'])
        ct = base64.b64decode(b64['ciphertext'])
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        data = json.loads(pt.decode('utf-8'))
        return data
    except Exception:
        return {}

def save_license(data: dict):
    """
    Save encrypted license data to license file
    """
    enc = encrypt_license_data(data)
    os.makedirs(os.path.dirname(LICENSE_FILE), exist_ok=True)
    with open(LICENSE_FILE, 'w') as f:
        f.write(enc)

def load_license() -> dict:
    """
    Load and decrypt license data from file
    """
    if not os.path.exists(LICENSE_FILE):
        return {}
    with open(LICENSE_FILE, 'r') as f:
        enc = f.read()
    return decrypt_license_data(enc)

def is_license_valid(license_data: dict) -> bool:
    """
    Validate license data: check hardware ID match and expiry date
    """
    if not license_data:
        return False
    hwid = get_hardware_id()
    if license_data.get('hwid') != hwid:
        return False
    expiry_str = license_data.get('expiry')
    if not expiry_str:
        return False
    try:
        expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")
        if expiry_date < datetime.now():
            return False
    except Exception:
        return False
    return True

def is_pro_user() -> bool:
    """
    Check if current user has valid Pro license
    """
    license_data = load_license()
    if not is_license_valid(license_data):
        return False
    return license_data.get('pro', False)

def get_license_remaining_days() -> int:
    """
    Get remaining days before license expiry
    """
    license_data = load_license()
    expiry_str = license_data.get('expiry')
    if not expiry_str:
        return 0
    try:
        expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")
        delta = expiry_date - datetime.now()
        return max(delta.days, 0)
    except Exception:
        return 0

def generate_license_key() -> str:
    """
    Generate a dummy license key in format XXXX-XXXX-XXXX-XXXX
    (For testing or demo purposes)
    """
    import random
    parts = []
    for _ in range(4):
        part = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))
        parts.append(part)
    return '-'.join(parts)

def validate_license_key_format(key: str) -> bool:
    """
    Validate license key format XXXX-XXXX-XXXX-XXXX
    """
    import re
    pattern = r'^[A-Z0-9]{4}(-[A-Z0-9]{4}){3}$'
    return bool(re.match(pattern, key.upper()))
