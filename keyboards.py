from aiogram.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton

web_button = (
    KeyboardButton(
        text="Открыть Web App",
        web_app=WebAppInfo(
        url= "URL_ngrok")
    )
)


wa_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[web_button]])