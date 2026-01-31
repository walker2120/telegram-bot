import os
import time
import requests

TOKEN = os.getenv("7737680916:AAF6uJpR5zgfC1EONbpbuIxmgy3Jk8vMS1Q")
CHAT_ID = os.getenv("1736924392")

URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(text):
    requests.post(
        f"{URL}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )

if __name__ == "__main__":
    send_message(" Bot activo en la nube")
    while True:
        time.sleep(60)
