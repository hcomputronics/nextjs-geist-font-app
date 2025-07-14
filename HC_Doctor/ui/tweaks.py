import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from tools import cleaner
from license import license_utils
import threading

class TweaksFrame(tb.Frame):
    def __init__(self, parent, is_pro):
        super().__init__(parent)
        self.is_pro = is_pro
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = tb.Label(self, text="Tweaks", font=("Segoe UI", 16, "bold"))
        self.lbl_title.pack(pady=10)

        # Simple tweaks (Free)
        self.chk_dark_mode_var = tk.BooleanVar(value=False)
        self.chk_dark_mode = tb.Checkbutton(self, text="Enable Dark Mode", variable=self.chk_dark_mode_var, bootstyle="info")
        self.chk_dark_mode.pack(anchor="w", padx=20, pady=5)

        self.chk_show_seconds_var = tk.BooleanVar(value=True)
        self.chk_show_seconds = tb.Checkbutton(self, text="Show Seconds in Clock", variable=self.chk_show_seconds_var, bootstyle="info")
        self.chk_show_seconds.pack(anchor="w", padx=20, pady=5)

        self.chk_bing_off_var = tk.BooleanVar(value=False)
        self.chk_bing_off = tb.Checkbutton(self, text="Disable Bing Search", variable=self.chk_bing_off_var, bootstyle="info")
        self.chk_bing_off.pack(anchor="w", padx=20, pady=5)

        # Pro tweaks
        if self.is_pro:
            self.chk_usb_block_var = tk.BooleanVar(value=False)
            self.chk_usb_block = tb.Checkbutton(self, text="Block USB Devices", variable=self.chk_usb_block_var, bootstyle="warning")
            self.chk_usb_block.pack(anchor="w", padx=20, pady=5)

            self.chk_webcam_mic_var = tk.BooleanVar(value=False)
            self.chk_webcam_mic = tb.Checkbutton(self, text="Disable Webcam and Microphone", variable=self.chk_webcam_mic_var, bootstyle="warning")
            self.chk_webcam_mic.pack(anchor="w", padx=20, pady=5)

            self.chk_disable_cmd_var = tk.BooleanVar(value=False)
            self.chk_disable_cmd = tb.Checkbutton(self, text="Disable Command Prompt", variable=self.chk_disable_cmd_var, bootstyle="warning")
            self.chk_disable_cmd.pack(anchor="w", padx=20, pady=5)
        else:
            self.lbl_pro_info = tb.Label(self, text="Upgrade to Pro to unlock all tweaks.", bootstyle="secondary")
            self.lbl_pro_info.pack(pady=10)

        self.btn_apply = tb.Button(self, text="Apply Tweaks", bootstyle="success", command=self.apply_tweaks)
        self.btn_apply.pack(pady=20)

    def apply_tweaks(self):
        # For demo, just show a message
        messagebox.showinfo("Tweaks", "Tweaks applied successfully (demo).")
