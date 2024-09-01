import websocket
import threading
import time
import re
import ctypes
from config import (
    CHANNEL,
    ALERT_SOUND,
    ALERT_RUMBLE,
    ICON_FILE,
    ICON_FILE2,
)
from alerts import sound, rumble

# Windows API constants and functions
ICON_SMALL = 0
ICON_BIG = 1
WM_SETICON = 0x0080
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32


class AnonymousTwitchChatReader:
    def __init__(
        self,
        channel,
        hwnd,
        icon1,
        icon2,
        sound,
        rumble,
    ):
        self.ws = None
        self.channel = channel.lower()
        self.hwnd = hwnd
        self.icon1 = icon1
        self.icon2 = icon2
        self.sound = sound
        self.rumble = rumble
        self.alert_sound = ALERT_SOUND
        self.alert_rumble = ALERT_RUMBLE
        self.sound_alerted = False

    def connect(self):
        self.ws = websocket.WebSocketApp(
            "wss://irc-ws.chat.twitch.tv:443",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        wst = threading.Thread(target=self.ws.run_forever)
        wst.daemon = True
        wst.start()
        self.set_taskbar_icon(self.icon1)

    def on_open(self, ws):
        print(f"Connected to #{self.channel}")
        self.ws.send(f"NICK justinfan12345")  # Use a random username
        self.ws.send(f"JOIN #{self.channel}")
        self.ws.send("CAP REQ :twitch.tv/tags twitch.tv/commands")

    def on_message(self, ws, message):
        if message.startswith("PING"):
            self.ws.send("PONG :tmi.twitch.tv")
        elif "PRIVMSG" in message:
            self.parse_message(message)
            self.update_taskbar_icon()

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("Connection closed")

    def parse_message(self, message):
        username_match = re.search(r"display-name=(\w+)", message)
        content_match = re.search(r"PRIVMSG.*:(.+)", message)

        if username_match and content_match:
            username = username_match.group(1)
            content = content_match.group(1)
            print(f"{username}: {content}")

    def is_window_visible_and_foreground(self):
        return (
            user32.IsWindowVisible(self.hwnd)
            and user32.GetForegroundWindow() == self.hwnd
        )

    def set_taskbar_icon(self, icon):
        user32.SendMessageW(self.hwnd, WM_SETICON, ICON_SMALL, icon)
        user32.SendMessageW(self.hwnd, WM_SETICON, ICON_BIG, icon)

    def update_taskbar_icon(self):
        if not self.is_window_visible_and_foreground():
            self.set_taskbar_icon(self.icon2)
            if self.alert_sound and not self.sound_alerted:
                self.sound.alert()
                self.sound_alerted = True
            if self.alert_rumble:
                self.rumble.alert()

    def disconnect(self):
        if self.ws:
            self.ws.close()


if __name__ == "__main__":
    HWND = kernel32.GetConsoleWindow()
    ICON1 = user32.LoadImageW(None, ICON_FILE, 1, 0, 0, 0x00000010)
    ICON2 = user32.LoadImageW(None, ICON_FILE2, 1, 0, 0, 0x00000010)

    reader = AnonymousTwitchChatReader(CHANNEL, HWND, ICON1, ICON2, sound, rumble)
    reader.connect()

    try:
        while True:
            if reader.is_window_visible_and_foreground():
                reader.set_taskbar_icon(ICON1)
                reader.sound_alerted = False
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Disconnecting...")
        reader.disconnect()
