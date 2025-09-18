import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=".send.env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(name, phone, email, message):
    text = (
        f"Yangi xabar keldi!\n\n"
        f"Ism: {name}\n"
        f"Telefon: {phone}\n"
        f"Email: {email}\n"
        f"Xabar: {message}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Telegramga yuborishda xato: {e}")
        return False
