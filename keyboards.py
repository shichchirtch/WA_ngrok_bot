from aiogram.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton

web_button = (
    KeyboardButton(
        text="Открыть Web App",
        web_app=WebAppInfo(
        url="https://b199-2a00-20-8-1dfb-3987-28ae-e765-37da.ngrok-free.app")
    )
)

wa_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[web_button]])