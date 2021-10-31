from app import bot, dp
from config import admin_id
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone

from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
   await bot.send_message(chat_id=admin_id, text="<i>Salom Raxmatjon bot ishga tushdi</i>", parse_mode='HTML')
@dp.message_handler()
async def echo(message: Message):
   chat_id = message["from"]["id"]
   text = message.text
   if text == '/start':
      await bot.send_message(chat_id=chat_id, text="Iltimos bir nima deb yozing!")
   elif text == '/admin' or text == '/help':
      await bot.send_message(chat_id=chat_id, text="<b>👤Admin: @xc_ho @ufo_607 . <pre>(24 soat ichida javob kelmasa qayta yozing <i>:)</i>)</pre>\n\n🤖Kanalimiz: @ufobots</b>", parse_mode='HTML')
   else:
      headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
      res = requests.get(
         f'https://www.google.com/search?q=urganch weather&oq=urganch weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
      soup = BeautifulSoup(res.text, 'html.parser')
#       time = soup.select('#wob_dts')[0].getText().strip()
      info = soup.select('#wob_dc')[0].getText().strip()
      weather = round((int(soup.select('#wob_tm')[0].getText().strip())-32)*(5/9))
      format = "%d-%m-%Y"
      format1 = "%H:%M"
      time = "%H:00"
      now_utc = datetime.now(timezone('UTC'))
      now_asia = now_utc.astimezone(timezone('Asia/Tashkent'))
      sana = now_asia.strftime(format)
      soat = now_asia.strftime(format1)
      await bot.send_message(chat_id=chat_id, text=f"<b>🏙Hudud: <i>Xorazm viloyati</i>\n\n📅Sana: <i>{sana}</i>\n\n⌚️Soat: <i>{soat}</i>\n\n🌡Havo harorati: <i>{weather}°C</i>\n\n🕐Yangilangan vaqt: <i>{time}</i></b>", parse_mode='HTML')
   
   # await message.answer(text=text)
