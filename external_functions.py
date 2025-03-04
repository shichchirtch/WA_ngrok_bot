from bot_instance import bot_tocken
import requests

BOT_URL = "http://127.0.0.1:8000/update_order"  # Эндпоинт бота для обновления данных

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{bot_tocken}/sendMessage"
    payload = {
        "chat_id": -4711453703,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)



def update_bot_database(user_id, address, phone, payment):
    """Отправляет данные в бота через его API."""
    payload = {"user_id": user_id, "address": address, "phone": phone, "payment": payment}
    try:
        requests.post(BOT_URL, json=payload)
    except Exception as e:
        print(f"Ошибка при отправке в бота: {e}")