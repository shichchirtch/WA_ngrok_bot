from aiogram.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton

web_button = (
    KeyboardButton(
        text="Открыть Web App",
        web_app=WebAppInfo(
        url="https://f1af-2a00-20-8-1dfb-c3-5496-c60c-67b1.ngrok-free.app")
    )
)


wa_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[web_button]])