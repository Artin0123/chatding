# chatding!

_A simple chat notifier for Twitch streamers without viewers_

Download/clone this repo and run dist/chatding.exe or run chatding.py  

make sure it work when launch first time.  

## Preamble

**chatding** is a utility designed for streamers with low or no audience alerting the user with an audible alarm when someone writes in the twitch chat.

### Set-up

channel name will saved in channel_name.txt

_Edit file config.py_

```
# pyinstaller -F .\chatding.py
# pyinstaller -F -w -n open_chatding .\open_chading.py

# Wait x seconds to play alert on new chat message
DELAY = 120

### Enable (True) / Disable (False) alert modules
# ALERT_SOUND plays audible alarm on default sound device
# ALERT_RUMBLE activate rumble on XBOX compatible controller, more settings in rumble.py
ALERT_SOUND = True
ALERT_RUMBLE = False

# Alert sound file in WAV format
SOUND_FILE = 'sounds/alert.wav'
```


### Behavior

**chatding** plays the alert when it detects a new message in the chat and waits the number of seconds specified in the DELAY variable for a new alert.

If the chatding window is in foreground no sound will be played (this feature only works on Windows platform).
