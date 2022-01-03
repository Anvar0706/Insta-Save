import requests
import re
import logging
from aiogram import Bot, Dispatcher, executor, types
def get_response(url):
    r = requests.get(url)
    while r.status_code !=200:
        r = requests.get(url)
    return r.text
def prepare_urls(matches):
    return list({match.replace("\\u0026","&") for match in matches})
API_TOKEN = '5033191251:AAGsYXY_5QSJ_m6JM0bP4YTfpqnawJWNxWc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Salom👋🏻👋🏻👋🏻 Insta save botiga xush kelibsiz. Bu bot orqali instagramdan fayllarni📄 yuklab olishingiz mumkin. Botga insatgramdagi video yoki rasm linkini📎 tashlang.")
@dp.message_handler()
async def src_send(message: types.Message):
    if message.text != "":
      url = message.text
      msgid = (await message.reply("Yuklanmoqda...🚀🚀🚀")).message_id
      response = get_response(url)
      vid_matches = re.findall('"video_url":"([^"]+)"', response)
      pic_matches = re.findall('"display_url":"([^"]+)"', response)
      vid_urls = prepare_urls(vid_matches)
      pic_urls = prepare_urls(pic_matches)
      # await message.answer(f"Video url: {vid_urls}\nPicture url: {pic_urls}")
      if vid_urls:
        await message.answer(f"Video ssilkasi: {vid_urls}\n.\n.\n.\n.\n@Insaveuzbot")
      elif pic_urls: 
        await message.answer(f"Rasm ssilkasi: {pic_urls}\n.\n.\n.\n.\n@Insaveuzbot") 
      elif not vid_urls or pic_urls:
        await message.answer("Link xato kiritilgan...")
      await bot.delete_message(chat_id=message.from_user.id, message_id=msgid)  
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
     # https://www.instagram.com/tv/CYIoTm8gbHb/?utm_medium=copy_link