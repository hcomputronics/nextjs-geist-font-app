import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from . import license_utils
import os
import json
from datetime import datetime, timedelta

class LicenseManagerFrame(tb.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.style = tb.Style()
        self.create_widgets()
        self.load_license_info()

    def create_widgets(self):
        self.lbl_title = tb.Label(self, text="License Activation", font=("Segoe UI", 16, "bold"))
        self.lbl_title.pack(pady=10)

        self.lbl_info = tb.Label(self, text="Enter your license key below to activate Pro features.\nLicense key format: XXXX-XXXX-XXXX-XXXX", wraplength=400)
        self.lbl_info.pack(pady=5)

        self.license_var = tk.StringVar()
        self.entry_license = tb.Entry(self, textvariable=self.license_var, width=30, bootstyle="info")
        self.entry_license.pack(pady=5)

        self.btn_activate = tb.Button(self, text="Activate", bootstyle="success", command=self.activate_license)
        self.btn_activate.pack(pady=10)

        self.lbl_status = tb.Label(self, text="", font=("Segoe UI", 12))
        self.lbl_status.pack(pady=5)

        self.btn_deactivate = tb.Button(self, text="Deactivate License", bootstyle="danger", command=self.deactivate_license)
        self.btn_deactivate.pack(pady=10)

    def load_license_info(self):
        license_data = license_utils.load_license()
        if license_utils.is_license_valid(license_data):
            days_left = license_utils.get_license_remaining_days()
            pro_status = "Pro" if license_data.get('pro', False) else "Free"
            self.lbl_status.config(text=f"License Active: {pro_status} User\nExpires in {days_left} day(s)")
            self.license_var.set(license_data.get('key', ''))
            self.app.is_pro = license_utils.is_pro_user()
        else:
            self.lbl_status.config(text="No valid license found. You are using Free version.")
            self.app.is_pro = False

    def activate_license(self):
        key = self.license_var.get().strip().upper()
        if not license_utils.validate_license_key_format(key):
            messagebox.showerror("Invalid Key", "License key format is invalid. Please enter a valid key.")
            return

        # For demo, accept any valid format key and create license data
        hwid = license_utils.get_hardware_id()
        expiry_date = datetime.now() + timedelta(days=365)  # 1 year license
        license_data = {
            "key": key,
            "hwid": hwid,
            "expiry": expiry_date.strftime("%Y-%m-%d"),
            "pro": True
        }
        license_utils.save_license(license_data)
        messagebox.showinfo("Activated", "License activated successfully! Please restart the app.")
        self.load_license_info()

    def deactivate_license(self):
        license_file = license_utils.LICENSE_FILE
        if os.path.exists(license_file):
            os.remove(license_file)
        messagebox.showinfo("Deactivated", "License deactivated. You are now using Free version.")
        self.license_var.set("")
        self.load_license_info()
