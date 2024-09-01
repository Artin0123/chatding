# pyinstaller -F .\chatding.py
# pyinstaller -F -w -n open_chatding .\open_chading.py

import os
import sys

# 假設 config.py 與 chatding.py 在同一目錄下
# 檢查程式是作為可執行檔運行還是作為腳本運行
if getattr(sys, "frozen", False):
    # 以下會以執行檔當前的目錄執行
    # 預設存在./dist
    BASE_DIR = os.path.dirname(os.path.dirname(sys.executable))
elif __file__:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

###以下為變數設定
# Your twitch channel name
CHANNEL = "artin0123"

### Enable (True) / Disable (False) alert modules
# ALERT_SOUND plays audible alarm on default sound device
# ALERT_RUMBLE activate rumble on XBOX compatible controller, more settings in rumble.py
ALERT_SOUND = True
ALERT_RUMBLE = False

SOUND_FILE = os.path.join(BASE_DIR, "sounds", "alert2.wav")

ICON_FILE = os.path.join(BASE_DIR, "icons", "icon1.ico")
ICON_FILE2 = os.path.join(BASE_DIR, "icons", "icon2.ico")
