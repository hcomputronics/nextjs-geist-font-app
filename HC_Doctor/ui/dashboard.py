import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import psutil
import GPUtil
import threading
import time

class DashboardFrame(tb.Frame):
    def __init__(self, parent, is_pro):
        super().__init__(parent)
        self.is_pro = is_pro
        self.style = tb.Style()
        self.create_widgets()
        self.update_stats()

    def create_widgets(self):
        self.lbl_title = tb.Label(self, text="Dashboard", font=("Segoe UI", 16, "bold"))
        self.lbl_title.pack(pady=10)

        self.cpu_label = tb.Label(self, text="CPU Usage: ", font=("Segoe UI", 12))
        self.cpu_label.pack(anchor="w", padx=20, pady=5)

        self.cpu_progress = tb.Progressbar(self, length=400, mode="determinate", bootstyle="info")
        self.cpu_progress.pack(padx=20, pady=5)

        self.ram_label = tb.Label(self, text="RAM Usage: ", font=("Segoe UI", 12))
        self.ram_label.pack(anchor="w", padx=20, pady=5)

        self.ram_progress = tb.Progressbar(self, length=400, mode="determinate", bootstyle="success")
        self.ram_progress.pack(padx=20, pady=5)

        self.disk_label = tb.Label(self, text="Disk Usage: ", font=("Segoe UI", 12))
        self.disk_label.pack(anchor="w", padx=20, pady=5)

        self.disk_progress = tb.Progressbar(self, length=400, mode="determinate", bootstyle="warning")
        self.disk_progress.pack(padx=20, pady=5)

        self.gpu_label = tb.Label(self, text="GPU Usage: ", font=("Segoe UI", 12))
        self.gpu_label.pack(anchor="w", padx=20, pady=5)

        self.gpu_progress = tb.Progressbar(self, length=400, mode="determinate", bootstyle="danger")
        self.gpu_progress.pack(padx=20, pady=5)

        self.uptime_label = tb.Label(self, text="System Uptime: ", font=("Segoe UI", 12))
        self.uptime_label.pack(anchor="w", padx=20, pady=10)

    def update_stats(self):
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        self.cpu_progress['value'] = cpu_percent

        # RAM usage
        ram = psutil.virtual_memory()
        ram_percent = ram.percent
        self.ram_label.config(text=f"RAM Usage: {ram_percent}% ({self._get_size(ram.used)} / {self._get_size(ram.total)})")
        self.ram_progress['value'] = ram_percent

        # Disk usage (C drive)
        disk = psutil.disk_usage('C:\\')
        disk_percent = disk.percent
        self.disk_label.config(text=f"Disk Usage (C:): {disk_percent}% ({self._get_size(disk.used)} / {self._get_size(disk.total)})")
        self.disk_progress['value'] = disk_percent

        # GPU usage
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            gpu_load = gpu.load * 100
            self.gpu_label.config(text=f"GPU Usage: {gpu_load:.1f}%")
            self.gpu_progress['value'] = gpu_load
        else:
            self.gpu_label.config(text="GPU Usage: N/A")
            self.gpu_progress['value'] = 0

        # Uptime
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_str = self._format_uptime(uptime_seconds)
        self.uptime_label.config(text=f"System Uptime: {uptime_str}")

        # Schedule next update
        self.after(2000, self.update_stats)

    def _get_size(self, bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor
        return f"{bytes:.2f}P{suffix}"

    def _format_uptime(self, seconds):
        days = int(seconds // (24 * 3600))
        seconds %= 24 * 3600
        hours = int(seconds // 3600)
        seconds %= 3600
        minutes = int(seconds // 60)
        return f"{days}d {hours}h {minutes}m"
