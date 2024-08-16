import os
import sys

# Your twitch channel preceded by a hash
CHANNEL = '#artin0123'

# Wait x seconds to play alert again on new chat message
DELAY = 0

### Enable (True) / Disable (False) alert modules
# ALERT_SOUND plays audible alarm on default sound device
# ALERT_RUMBLE activate rumble on XBOX compatible controller, more settings in rumble.py
ALERT_SOUND = False
ALERT_RUMBLE = False

# 假設 config.py 與 chatding.py 在同一目錄下
# 檢查程式是作為可執行檔運行還是作為腳本運行
if getattr(sys, 'frozen', False):
    # 以下會以執行檔當前的目錄執行
    # pyinstaller.exe -F .\chatding.py
    # 預設存在./dist
    BASE_DIR = os.path.dirname(os.path.dirname(sys.executable))
elif __file__:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOUND_FILE = os.path.join(BASE_DIR, 'sounds', 'alert2.wav')

ICON_FILE = os.path.join(BASE_DIR, "icons", "icon1.ico")
ICON_FILE2 = os.path.join(BASE_DIR, "icons", "icon2.ico")
