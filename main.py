from command_handlers import ch_router
# from start_menu import set_main_menu
from bot_instance import bot, bot_storage_key, dp
from  app import app
import threading, asyncio

def run_flask():
    app.run(host="0.0.0.0", port=5000, debug=False)  # ОТКЛЮЧИ debug=True!
    # 127.0.0.1:4040

async def main():
    await dp.storage.set_data(key=bot_storage_key, data={})
    # await set_main_menu(bot)
    dp.include_router(ch_router)
    # Запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    # Запускаем Flask в отдельном потоке
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    # Запускаем асинхронного бота
    asyncio.run(main())


