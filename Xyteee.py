import os, sys
os.system('xdg-open https://whatsapp.com/channel/0029VaXTSiI2phHGeH8Wd23r')
try:
    __import__("FbA").security()
except Exception as e:
    exit(str(e))
