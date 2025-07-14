import subprocess

def run_sfc_scan():
    try:
        result = subprocess.run(["sfc", "/scannow"], capture_output=True, text=True, shell=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

def repair_print_spooler():
    try:
        cmds = [
            "net stop spooler",
            "del /Q /F %systemroot%\\System32\\spool\\PRINTERS\\*.*",
            "net start spooler"
        ]
        for cmd in cmds:
            subprocess.run(cmd, shell=True)
        return "Print Spooler repaired successfully."
    except Exception as e:
        return str(e)

def reset_windows_store():
    try:
        cmd = "powershell -Command \"Get-AppxPackage -allusers Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register '$($_.InstallLocation)\\AppXManifest.xml'}\""
        subprocess.run(cmd, shell=True)
        return "Windows Store reset successfully."
    except Exception as e:
        return str(e)
