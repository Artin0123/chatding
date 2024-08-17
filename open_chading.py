from config import BASE_DIR
import subprocess
import os
import sys

# 構建 chatding.exe 的完整路徑
open_chading_path = os.path.join(BASE_DIR, "dist", "chatding.exe")

# 啟動 chatding.exe
subprocess.Popen([open_chading_path] + sys.argv[1:])
