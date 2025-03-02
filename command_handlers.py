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
        await state.set_data({'card_list':[], 'cart_pos':0, 'timer':0, 'leader':0})
        await message.answer(text=f'{html.bold(html.quote(user_name))}, '
                                  f'Hallo !\nI am MINI APP Bot'
                                  f'🎲',
                             parse_mode=ParseMode.HTML)
        await message.answer("Нажми на кнопку, чтобы открыть приложение!", reply_markup=wa_kb)
    else:
        print("else works")


@ch_router.message(Command('send'))
async def send_command(message: Message, state: FSMContext):
    await state.set_state(FSM_ST.swnd_msg)
    await message.answer('Enter you message')

# First Accaunt = 6685637602
# Second Accaunt = 6831521683

@ch_router.message(StateFilter(FSM_ST.swnd_msg))
async def sending_msg_other_user(message: Message, state: FSMContext):
    prefix, us_id, text_msg = message.text.split('$')
    user_id = int(us_id)
    try:
        await bot.send_message(chat_id=user_id, text=text_msg)
        await message.answer('Message is sent !')
    except Exception as e:
        await message.answer(f'Msg is not sent due to {e}')
    await state.set_state(FSM_ST.after_start)


# @ch_router.message()
# async def handle_web_app_data(msg: Message):
#     print(msg)  # Выводим весь msg для анализа
#     if msg.web_app_data:
#         print('we are hier')
#         data = msg.web_app_data.data
#         await msg.answer(f"Вы отправили: {data}")
#     else:
#         await msg.answer("Данные не найдены!")

# curl https://api.telegram.org/bot7961544857:AAGoiBeimCnjEL2fbixAxRHUipBKVFHi2bg/getUpdates

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