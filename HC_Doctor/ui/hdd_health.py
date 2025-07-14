import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tools import health_utils
import threading

class HDDHealthFrame(tb.Frame):
    def __init__(self, parent, is_pro):
        super().__init__(parent)
        self.is_pro = is_pro
        self.create_widgets()
        self.update_health()

    def create_widgets(self):
        self.lbl_title = tb.Label(self, text="HDD Health Monitor", font=("Segoe UI", 16, "bold"))
        self.lbl_title.pack(pady=10)

        self.health_text = tb.Text(self, height=20, width=80, state="disabled", bootstyle="secondary")
        self.health_text.pack(padx=10, pady=10)

    def update_health(self):
        def task():
            health_info = health_utils.get_hdd_health()
            self.health_text.config(state="normal")
            self.health_text.delete("1.0", tk.END)
            self.health_text.insert(tk.END, health_info)
            self.health_text.config(state="disabled")
        threading.Thread(target=task).start()
        self.after(10000, self.update_health)  # update every 10 seconds
