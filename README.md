# chatding!

_A simple chat notifier for Twitch streamers without viewers_

Download/clone this repo and run dist/chatding.exe or run chatding.py  

make sure it work when launch first time.  

## Preamble

**chatding** is a utility designed for streamers with low or no audience alerting the user with an audible alarm when someone writes in the twitch chat.

### Set-up


使用git clone取得此repo，再使用venv的pyinstaller更改config.py

_Edit file config.py_

```
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
```
更改完config後，終端機執行以下程式碼 (假設環境為PowerShell)

chatding!的作用在於建立chatding!.exe的捷徑後，不需在dist路徑下開啟，也可以釘選到開始 (chatding.exe的捷徑無法更改工作列圖示)
```
.\.venv\Scripts\Activate.ps1
pyinstaller -F .\chatding.py
pyinstaller -F -w -n chatding! .\chatding!.py
deactivate
```
之後執行 chatding!.exe 或 它的捷徑

### Behavior

**chatding** plays the alert when it detects a new message in the chat.

If the chatding window is in foreground no sound will be played (this feature only works on Windows platform).
