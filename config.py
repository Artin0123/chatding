import os

# Your twitch channel preceded by a hash
CHANNEL = '#artin0123'

# Wait x seconds to play alert again on new chat message
DELAY = 2

### Enable (True) / Disable (False) alert modules
# ALERT_SOUND plays audible alarm on default sound device
# ALERT_RUMBLE activate rumble on XBOX compatible controller, more settings in rumble.py
ALERT_SOUND = True
ALERT_RUMBLE = False

# 假設 config.py 與 chatding.py 在同一目錄下
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_FILE = os.path.join(BASE_DIR, 'sounds', 'alert2.wav')
