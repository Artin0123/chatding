# chatding!

_A simple chat notifier for Twitch streamers without viewers_

## Preamble

**chatding** is a utility designed for streamers with low or no audience alerting the user with an audible alarm when someone writes in the twitch chat.

### Set-up

Download/clone this repo and run dist/chatding.exe or run chatding.py  

make sure it work when launch first time.

### Behavior

**chatding** plays the alert when it detects a new message in the chat and waits the number of seconds specified in the DELAY variable for a new alert.

If the chatding window is in foreground no sound will be played (this feature only works on Windows platform).
