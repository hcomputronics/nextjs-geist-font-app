import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tools import cleaner, sfc_tool
from tkinter import messagebox
import threading

class OptimizationFrame(tb.Frame):
    def __init__(self, parent, is_pro):
        super().__init__(parent)
        self.is_pro = is_pro
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = tb.Label(self, text="Optimization", font=("Segoe UI", 16, "bold"))
        self.lbl_title.pack(pady=10)

        self.btn_junk_cleaner = tb.Button(self, text="Run Junk Cleaner", bootstyle="success", command=self.run_junk_cleaner)
        self.btn_junk_cleaner.pack(pady=10)

        self.btn_sfc_scan = tb.Button(self, text="Run SFC Scan", bootstyle="info", command=self.run_sfc_scan)
        self.btn_sfc_scan.pack(pady=10)

    def run_junk_cleaner(self):
        def task():
            self.btn_junk_cleaner.config(state="disabled")
            cleaner.clean_junk()
            messagebox.showinfo("Junk Cleaner", "Junk cleaning completed.")
            self.btn_junk_cleaner.config(state="normal")
        threading.Thread(target=task).start()

    def run_sfc_scan(self):
        def task():
            self.btn_sfc_scan.config(state="disabled")
            output = sfc_tool.run_sfc_scan()
            messagebox.showinfo("SFC Scan Result", output)
            self.btn_sfc_scan.config(state="normal")
        threading.Thread(target=task).start()

class CleanRepairFrame(tb.Frame):
    def __init__(self, parent, is_pro):
        super().__init__(parent)
        self.is_pro = is_pro
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = tb.Label(self, text="Clean & Repair", font=("Segoe UI", 16, "bold"))
        self.lbl_title.pack(pady=10)

        self.btn_repair_print_spooler = tb.Button(self, text="Repair Print Spooler", bootstyle="warning", command=self.repair_print_spooler)
        self.btn_repair_print_spooler.pack(pady=10)

        self.btn_reset_store = tb.Button(self, text="Reset Windows Store", bootstyle="warning", command=self.reset_store)
        self.btn_reset_store.pack(pady=10)

    def repair_print_spooler(self):
        def task():
            self.btn_repair_print_spooler.config(state="disabled")
            output = sfc_tool.repair_print_spooler()
            messagebox.showinfo("Repair Print Spooler", output)
            self.btn_repair_print_spooler.config(state="normal")
        threading.Thread(target=task).start()

    def reset_store(self):
        def task():
            self.btn_reset_store.config(state="disabled")
            output = sfc_tool.reset_windows_store()
            messagebox.showinfo("Reset Windows Store", output)
            self.btn_reset_store.config(state="normal")
        threading.Thread(target=task).start()
