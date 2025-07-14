import os
import shutil
import ctypes
import tempfile
import subprocess

def clean_temp():
    temp_dir = tempfile.gettempdir()
    try:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception:
                    pass
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))
                except Exception:
                    pass
        return True
    except Exception:
        return False

def clean_prefetch():
    prefetch_dir = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Prefetch')
    try:
        for file in os.listdir(prefetch_dir):
            file_path = os.path.join(prefetch_dir, file)
            try:
                os.remove(file_path)
            except Exception:
                pass
        return True
    except Exception:
        return False

def clean_recycle_bin():
    try:
        # Using ctypes to empty recycle bin
        SHERB_NOCONFIRMATION = 0x00000001
        SHERB_NOPROGRESSUI = 0x00000002
        SHERB_NOSOUND = 0x00000004
        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)
        return result == 0
    except Exception:
        return False

def clean_junk():
    clean_temp()
    clean_prefetch()
    clean_recycle_bin()
