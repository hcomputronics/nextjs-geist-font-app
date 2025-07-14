import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tools import disk_tools
from tkinter import messagebox
import threading

class LowLevelFormatFrame(tb.Frame):
    def __init__(self, parent, is_pro):
        super().__init__(parent)
        self.is_pro = is_pro
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = tb.Label(self, text="Low Level Format Tool", font=("Segoe UI", 16, "bold"))
        self.lbl_title.pack(pady=10)

        self.lbl_info = tb.Label(self, text="Select the drive to perform low level format.\nThis operation is slow and will erase all data.", wraplength=400)
        self.lbl_info.pack(pady=5)

        self.drive_var = tk.StringVar()
        self.entry_drive = tb.Entry(self, textvariable=self.drive_var, width=10, bootstyle="info")
        self.entry_drive.pack(pady=5)
        self.entry_drive.insert(0, "E:")

        self.btn_format = tb.Button(self, text="Start Low Level Format", bootstyle="danger", command=self.start_format)
        self.btn_format.pack(pady=10)

    def start_format(self):
        drive = self.drive_var.get().strip()
        if not drive:
            messagebox.showerror("Error", "Please enter a drive letter (e.g. E:)")
            return

        def task():
            self.btn_format.config(state="disabled")
            success, msg = disk_tools.low_level_format(drive)
            if success:
                messagebox.showinfo("Success", f"Low level format completed on {drive}")
            else:
                messagebox.showerror("Error", f"Low level format failed: {msg}")
            self.btn_format.config(state="normal")

        threading.Thread(target=task).start()
