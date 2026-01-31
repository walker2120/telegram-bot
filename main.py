import os
import time
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(text):
    requests.post(
        f"{URL}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )

if name == "__main__":
    send_message("🤖 Bot activo en la nube. Todo listo 🚀")
    while True:
        time.sleep(60)
