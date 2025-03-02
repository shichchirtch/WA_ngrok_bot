from bot_instance import bot_tocken
import requests


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{bot_tocken}/sendMessage"
    payload = {
        "chat_id": -4711453703,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)