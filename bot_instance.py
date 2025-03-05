from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage, StorageKey
from fastapi import FastAPI, Request


class FSM_ST(StatesGroup):
    after_start = State()
    swnd_msg = State()


bot_tocken = '<BOT_TOKEN>'

bot = Bot(token=bot_tocken,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
aio_storage =MemoryStorage()

bot_storage_key = StorageKey(bot_id=bot.id, user_id=bot.id, chat_id=bot.id)

dp = Dispatcher(storage=aio_storage)
from fastapi import FastAPI, Request
api = FastAPI()

@api.post("/update_order")
async def update_order(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    address = data.get("address")
    phone = data.get("phone")
    payment = data.get("payment")

    if not user_id:
        return {"success": False, "error": "user_id не найден"}

    # Загружаем данные бота
    bot_dict = await dp.storage.get_data(key=bot_storage_key)

    if user_id not in bot_dict:
        bot_dict[user_id] = {"name": "Unknown", "order": {}}

    # Обновляем заказ
    bot_dict[user_id]["order"] = {"address": address, "phone": phone, "payment": payment}

    # Сохраняем обновлённые данные
    await dp.storage.update_data(key=bot_storage_key, data=bot_dict)

    return {"success": True}