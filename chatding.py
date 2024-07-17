import socket, time
from config import DELAY, CHANNEL, ALERT_SOUND, ALERT_RUMBLE, BASE_DIR, SOUND_FILE
from alerts import sound, rumble
from common import window
import os

print("First time setting")
# 假設 BASE_DIR 已經在 config.py 中定義
channel_file_path = os.path.join(BASE_DIR, 'channel_name.txt')

# 檢查 channel_name.txt 檔案是否存在
if not os.path.exists(channel_file_path):
    # 如果檔案不存在，提示用戶輸入頻道名稱
    channel_name = input("Input Twitch channel name: ")
    # 將頻道名稱寫入檔案
    with open(channel_file_path, 'w') as file:
        file.write(channel_name)
    # 更新 CHANNEL 變數
    CHANNEL = '#' + channel_name
else:
    # 如果檔案存在，從檔案讀取頻道名稱
    with open(channel_file_path, 'r') as file:
        CHANNEL = '#' + file.read().strip()

sock = socket.socket()
sock.connect(('irc.chat.twitch.tv', 6667))
sock.send(f"NICK justinfan0\n".encode('utf-8'))
sock.send(f"JOIN {CHANNEL}\n".encode('utf-8'))
sock.setblocking(0)  # 設置 socket 為非阻塞模式

lastAlert = 0

def parseChat(resp):
    resp = resp.rstrip().split('\r\n')
    for line in resp:
        if "PRIVMSG" in line:
            user = line.split(':')[1].split('!')[0]
            msg = line.split(':', maxsplit=2)[2]
            line = user + ": " + msg
        print(line)

try:
    while True:
        try:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
            
            elif len(resp) > 0:
                parseChat(resp)
                if not window.foreground() and time.time() - lastAlert > DELAY:
                    if ALERT_SOUND: 
                        sound.alert()
                        # print(SOUND_FILE)
                    if ALERT_RUMBLE: rumble.alert()
                    lastAlert = time.time()
        
        except BlockingIOError:
            # 當沒有數據可讀時，捕獲 BlockingIOError 並繼續迴圈
            pass
        
        time.sleep(1)  # 每1秒檢查一次
        pass

except KeyboardInterrupt:
    print("Program exited gracefully")
    sock.close()
    