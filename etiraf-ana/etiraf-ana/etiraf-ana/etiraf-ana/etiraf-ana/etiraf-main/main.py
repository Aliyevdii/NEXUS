from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
KANAL_ID = os.getenv("KANAL_ID")

IT = Client(
	"İtiraf Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN
	)

CHL = -1001617550080

PM = 2066118611

@IT.on_message(
	filters.command("start")
	& filters.private
	)
async def start(client: IT, message: Message):
	await message.reply_text(f"<b> {message.from_user.mention} Xos Geldin Men @A_l_i_y_e_v_d_i terefinden haz?rlanan bir etiraf botuyam.\nEtiraflar?n?z @Nexus_Etiraf_kanal kanal?nsa paylas?lacaq.\n\nSende bir etiraf etmek isteyirsen se komutlar;\nGizli Etiraf: /ano mesaj\nAc?q Etiraf: /etiraf mesaj</b>")

@IT.on_message(
	filters.command("ano")
	& filters.private
	)
async def ano(client: IT, message: Message):
	text = " ".join(message.command[1:])
	if text == "":
		await message.reply_text("Xahis Olunur Bir Etiraf yaz?b yeniden cehd edin.")
	else:
		await IT.send_message(chat_id=CHL, text=f"Gonderilen: ANON?M\nEtiraf: {text}")
		time.sleep(0.5)
		await IT.send_message(chat_id=PM, text=f"Gonderilen: {message.from_user.mention}\nEtiraf: {text}")
		time.sleep(0.5)
		await message.reply_text("Etiraflar?n?z?nSahibime gonderildi testik etdikdikten sonra @Nexus_Etiraf_kanal kanal?nda paylasilanaq.")

@IT.on_message(
	filters.command("etiraf")
	& filters.private
	)
async def etf(client: IT, message: Message):
	t = " ".join(message.command[1:])
	if t == "":
		await message.reply_text("Xahis Olunur Bir Etiraf yaz?b yeniden cehd edin.")
	else:
		await IT.send_message(chat_id=CHL, text=f"Gonderilen: {message.from_user.mention}\nEtiraf: {t}")
		time.sleep(0.5)
		await message.reply_text("Etiraflar?n?z?nSahibime gonderildi testik etdikdikten sonra @Nexus_Etiraf_kanal kanal?nda paylasilanaq.")

IT.run()
