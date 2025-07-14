# 🖥️ HC Doctor – System Health & Optimization Suite (by Harsh Computronics)

## Overview
HC Doctor is a powerful offline PC health, optimization, repair, and tweak tool for Windows 10/11. It offers both Free and Pro features with real-time hardware monitoring, system repair tools, and an offline license system.

## Features

### Free Features
- Dashboard with CPU, RAM, Disk, GPU stats using psutil & GPUtil
- System uptime, temperature, live usage bars
- Junk cleaner (Temp, Prefetch, Recycle Bin)
- Run SFC/DISM scans
- Repair print spooler, reset Windows Store
- Simple tweaks (dark mode, show seconds, disable Bing)
- Basic USB repair, low level format (slow), file preview
- Data recovery scan only (recovery locked)
- Two themes: Light and Dark

### Pro Features
- Full recovery unlock
- USB RAW fix, fast format
- Partition manager
- Registry cleaner
- Auto clean on boot
- All tweaks (USB block, webcam/mic rules, disable CMD)
- Save layout, full theme library
- Smart alerts, Pro badge
- Privacy log, App Lock
- Gamified UX (XP, badges)

## License System
- Offline activation with license key (XXXX-XXXX-XXXX-XXXX)
- Hardware ID binding (MAC + BIOS UUID)
- AES encrypted license file stored locally
- License validation on every launch
- Expiry date and remaining days display

## Installation

1. Install Python 3.8+ on Windows 10/11
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python main.py
   ```

## Packaging with PyInstaller

To create a standalone Windows executable:

```
pyinstaller --noconsole --icon=assets/icon.ico --name=HC_Doctor main.py
```

This will generate a `dist/HC_Doctor` folder with the executable.

## Folder Structure

```
HC_Doctor/
├── main.py
├── license/
│   ├── license_manager.py
│   └── license_utils.py
├── ui/
│   ├── dashboard.py
│   ├── optimization.py
│   ├── hdd_health.py
│   ├── low_level_format.py
│   └── tweaks.py
├── tools/
│   ├── sfc_tool.py
│   ├── cleaner.py
│   ├── disk_tools.py
│   └── health_utils.py
├── assets/
│   ├── icon.ico
│   └── styles.json
├── data/
│   ├── license.lic
│   └── config.json
├── README.md
└── requirements.txt
```

## Notes

- Replace `assets/icon.ico` with your own application icon.
- The license system is offline and secure.
- Pro features require valid license activation.

## Author

Harsh Computronics
