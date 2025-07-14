import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from license import license_utils
from ui import dashboard, optimization, hdd_health, low_level_format, tweaks
from license import license_manager
import os

class HCDoctorApp(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("🖥️ HC Doctor – System Health & Optimization Suite (by Harsh Computronics)")
        self.geometry("1000x700")
        self.minsize(900, 600)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Initialize license status
        self.is_pro = license_utils.is_pro_user()

        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Sidebar frame
        self.sidebar = tb.Frame(self, width=200, bootstyle="secondary")
        self.sidebar.grid(row=1, column=0, sticky="ns")
        self.sidebar.grid_propagate(False)

        # Top bar frame
        self.topbar = tb.Frame(self, height=50, bootstyle="primary")
        self.topbar.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.topbar.grid_propagate(False)

        # Content frame
        self.content = tb.Frame(self, bootstyle="light")
        self.content.grid(row=1, column=1, sticky="nsew")

        # App name label in top bar
        self.app_name_label = tb.Label(self.topbar, text="🖥️ HC Doctor – System Health & Optimization Suite", font=("Segoe UI", 14, "bold"), bootstyle="inverse")
        self.app_name_label.pack(side="left", padx=10)

        # Theme switch in top bar
        self.theme_var = tk.StringVar(value=self.style.theme_use())
        self.theme_switch = tb.Checkbutton(self.topbar, text="Dark Mode", variable=self.theme_var, onvalue="darkly", offvalue="flatly", bootstyle="success")
        self.theme_switch.pack(side="right", padx=10)
        self.theme_switch.configure(command=self.toggle_theme)

        # Sidebar buttons
        self.menu_buttons = {}
        menu_items = [
            ("Dashboard", self.show_dashboard),
            ("Optimization", self.show_optimization),
            ("Clean & Repair", self.show_clean_repair),
            ("HDD Monitor", self.show_hdd_health),
            ("Format Tool", self.show_format_tool),
            ("License", self.show_license),
            ("Settings", self.show_settings),
        ]
        for idx, (text, cmd) in enumerate(menu_items):
            btn = tb.Button(self.sidebar, text=text, bootstyle="info-outline", command=cmd)
            btn.pack(fill="x", pady=5, padx=10)
            self.menu_buttons[text] = btn

        # Initialize frames dict
        self.frames = {}

        # Show dashboard by default
        self.show_dashboard()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()
        frame = dashboard.DashboardFrame(self.content, self.is_pro)
        frame.pack(fill="both", expand=True)

    def show_optimization(self):
        self.clear_content()
        frame = optimization.OptimizationFrame(self.content, self.is_pro)
        frame.pack(fill="both", expand=True)

    def show_clean_repair(self):
        self.clear_content()
        frame = optimization.CleanRepairFrame(self.content, self.is_pro)
        frame.pack(fill="both", expand=True)

    def show_hdd_health(self):
        self.clear_content()
        frame = hdd_health.HDDHealthFrame(self.content, self.is_pro)
        frame.pack(fill="both", expand=True)

    def show_format_tool(self):
        self.clear_content()
        frame = low_level_format.LowLevelFormatFrame(self.content, self.is_pro)
        frame.pack(fill="both", expand=True)

    def show_license(self):
        self.clear_content()
        frame = license_manager.LicenseManagerFrame(self.content, self)
        frame.pack(fill="both", expand=True)

    def show_settings(self):
        self.clear_content()
        frame = tweaks.TweaksFrame(self.content, self.is_pro)
        frame.pack(fill="both", expand=True)

    def toggle_theme(self):
        new_theme = self.theme_var.get()
        self.style.theme_use(new_theme)

    def on_close(self):
        self.destroy()

if __name__ == "__main__":
    app = HCDoctorApp()
    app.mainloop()
