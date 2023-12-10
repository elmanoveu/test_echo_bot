import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '286674006:AAHDI3KvaBQcMlxDrE8NTmfgdSE4JvBShEc'

# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Эхо-обработчик всех текстовых сообщений
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
