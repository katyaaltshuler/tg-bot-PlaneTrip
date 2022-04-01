from telebot import types
import logging
import aiohttp
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import exceptions
from messages import Messages
from validators import Validators
import os

msg = Messages()
valid = Validators()

logging.basicConfig(level=logging.INFO)
load_dotenv('.env')

TOKEN = os.getenv("SECRET_TOKEN")
TELEGRAM_USER_ID = os.getenv("USER_ID")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# ---------------Set Access----------------------------
def auth(func):
    """Set single Access to the bot by User ID"""
    #---restriction is currently lifted up---
    async def wrapper(message):
        if message['from']['id'] != int(TELEGRAM_USER_ID):
            return await message.reply(msg.denied, reply=False)
        return await func(message)

    return wrapper


# --------Offer a list of commands available------------
@dp.message_handler(commands=['start'])
#@auth
async def send_welcome(message: types.Message):
    await message.answer(msg.greeting, parse_mode='html', reply=False)


# ---------Ask user's desired destination-------------------
@dp.message_handler(lambda message: message.text.startswith('/search_destination'))
#@auth
async def search_destination(message: types.Message):
    await message.answer(msg.ask_destination, parse_mode='html', reply=False)


# ---------Ask date interval(+ days of stay if round), parse--------------
@dp.message_handler(lambda message: 'round' in message.text.lower() or 'oneway' in message.text.lower())
#@auth
async def set_date_interval(message: types.Message):
    try:
        valid.parse_first_message(message.text)
        if valid.check_flight_type(message.text) == 'round':
            await message.answer(msg.ask_round_date_interval, parse_mode='html', reply=False)
        else:
            await message.answer(msg.ask_oneway_date_interval, parse_mode='html', reply=False)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return


# --------------Ask lowest acceptable price, parse-------------------
@dp.message_handler(lambda message: '/' in message.text or 'min' in message.text)
#@auth
async def set_max_price(message: types.Message):
    await message.answer(msg.ask_price, parse_mode='html', reply=False)
    try:
        valid.parse_second_message(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return


# --------Show request summary; last parse and send data to API---------------
@dp.message_handler(lambda message: 'eur' in message.text.lower() or 'usd' in message.text.lower())
#@auth
async def confirm_request(message: types.Message):
    try:
        valid.parse_last_message(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Yes, search my Trip', callback_data='get_results')
    item2 = types.InlineKeyboardButton('No, I want to edit this Trip', callback_data='/search_destination')
    markup.add(item1, item2)
    await message.answer(f'Well done! Is new Trip correct?\n\n'
                         f'{valid.flight_type.capitalize()} flight {valid.departure} to {valid.arrival} '
                         f'within period from {valid.from_date} to {valid.return_date} with price up to '
                         f'{valid.price} {valid.currency}.', parse_mode='html', reply=False, reply_markup=markup)


# -----------------Final results got from API-------------------
@dp.callback_query_handler(lambda call: True)
#@auth
async def get_results(call):
    if call.message:
        if call.data == "get_results":
            if valid.pull_data_to_search() is None:
                await call.message.answer(msg.unsuccessful_result, parse_mode='html', reply=False)
            else:
                flight_type, departure_city, departure_air, arrival_city, arrival_air, departure_date, lowest_price, \
                currency, url = valid.pull_data_to_search()
                await call.message.answer(f'Hey! I found something interesting for you!\n\n'
                                          f'{flight_type.capitalize()} flight {departure_city} ({departure_air}) to'
                                          f' {arrival_city} '
                                          f'({arrival_air})'
                                          f' departure on {departure_date} at a great price '
                                          f'{lowest_price} {currency.upper()}\nHurry up and <a href="{url}">'
                                          f'complete your booking here 🥝 </a>\n\nDon\'t like it? Start new '
                                          f'/search_destination!\n\nyour PlaneTrip bot', parse_mode='html',
                                          reply=False)
        else:
            await call.message.answer(msg.ask_destination, parse_mode='html', reply=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
