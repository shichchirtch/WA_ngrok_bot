from aiogram import Router, html, F
import asyncio
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove, Update, CallbackQuery
from aiogram.filters import CommandStart, Command, StateFilter
from python_db import user_dict, users_db
from copy import deepcopy
from aiogram.fsm.context import FSMContext
from bot_instance import bot, bot_storage_key, dp, FSM_ST
from keyboards import wa_kb
ch_router = Router()

@ch_router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    user_name = message.from_user.first_name
    if message.from_user.id not in users_db:
        print(message.from_user.id)
        users_db[message.from_user.id] = deepcopy(user_dict)
        await state.set_state(FSM_ST.after_start)
        bot_dict = await dp.storage.get_data(key=bot_storage_key)  # Получаю словарь бота
        bot_dict[message.from_user.id] = {'name':user_name, 'order':{}}  # Создаю пустой словарь для заметок юзера
        await dp.storage.update_data(key=bot_storage_key, data=bot_dict)  # Обновляю словарь бота
        await message.answer(text=f'{html.bold(html.quote(user_name))}, '
                                  f'Hallo !\nI am MINI APP Bot'
                                  f'🎲',
                             parse_mode=ParseMode.HTML)
        await message.answer("Нажми на кнопку, чтобы открыть приложение!", reply_markup=wa_kb)
    else:
        print("else works")


@ch_router.message(Command('help'))
async def help_command(message: Message, state: FSMContext):
    user_id = message.from_user.id
    temp_data = users_db[user_id]['bot_answer']
    if temp_data:
        await temp_data.delete()
    att = await message.answer('help')
    users_db[user_id]['bot_answer'] = att
    await asyncio.sleep(2)
    await message.delete()


@ch_router.message()
async def trasher(message: Message):
    print('TRASHER')
    await asyncio.sleep(1)
    await message.delete()