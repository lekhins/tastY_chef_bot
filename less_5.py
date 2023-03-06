from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '6197159674:AAH7P8dPsMGfNoL7cwdeHSLddcSDjO0perw'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот был успешно активирован')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>Привет, добро пжлвать в наш бот!</em>', parse_mode='HTML')


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEIBcdkBY_d_yJYkaw5eR0U6MTTYrLTowACiREAAjyzxQd3XR46Pa5Dbi4E')
    await message.delete()


@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply((message.text + "❤️"))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
