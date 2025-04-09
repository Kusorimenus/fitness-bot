from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = '7556658273:AAF4dXbTXIdBH1m7x0JnNw4LrzcTYD-aj5Q'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в *PowerSports* — место, где твое тело становится сильнее, а дух — непобедимым! 💪🔥\n\n"
        "Вот что я умею:\n"
        "• /train — записаться на тренировку 🏋️‍♂️\n"
        "• /abonement — купить абонемент 🧾",
        parse_mode="Markdown"
    )

@dp.message_handler(commands=['train'])
async def handle_train(message: Message):
    await message.answer("✅ Запись на тренировку успешно оформлена. Вы выбрали тренировку на этой неделе.")

@dp.message_handler(commands=['abonement'])
async def handle_abonement(message: Message):
    await message.answer("💳 Абонемент успешно приобретен. Вы выбрали один из доступных вариантов с соответствующими привилегиями.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
