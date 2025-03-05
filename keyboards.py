from aiogram.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton

web_button = (
    KeyboardButton(
        text="Открыть Web App",
        web_app=WebAppInfo(
        url="https://fcae-2a00-20-8-1dfb-3db8-b933-7e45-f0ad.ngrok-free.app")
    )
)

wa_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[web_button]])