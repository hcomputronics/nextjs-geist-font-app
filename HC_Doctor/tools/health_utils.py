import psutil
import GPUtil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    ram = psutil.virtual_memory()
    return ram.percent, ram.used, ram.total

def get_disk_usage(drive='C:\\'):
    disk = psutil.disk_usage(drive)
    return disk.percent, disk.used, disk.total

def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        return gpu.load * 100
    return None

def get_hdd_health():
    # Placeholder: Real HDD health requires SMART data reading
    return "HDD Health monitoring is under development."
