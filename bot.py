#    This file is part of the ChannelAutoForwarder distribution (https://github.com/Benchamxd/Telegraph-Uploader).
#    Copyright (c) 2021 Rithunand
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/MoTechYT/MT-Telegraph-Uploader/blob/main/License> 

import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery)

Mo_tech_mrk_yt = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Mo_tech_mrk_yt.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ🙃`")
  userid = str(message.chat.id)
  img_path = (f"./Download....!/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`Uploading.....🔥`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong🧐`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@Mo_tech_mrk_yt.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ🙃`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....🔥`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong🧐...") 
  else:
    await message.reply_text("Hmm Size Should Be Less Than 5 mb")

@Mo_tech_mrk_yt.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ🙃`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ🔥.....`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong🧐...") 
  else:
    await message.reply_text("Da Mowne Size Should Be Less Than 5 mb")

@Mo_tech_mrk_yt.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('🤔ᕼᗴᒪᑭ', callback_data='help'),
        InlineKeyboardButton('ℭ𝔩𝔬𝔰𝔢🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('ᗰᗝᐯᎥᗴ Ǥᖇᗝᑌᑭ🎬', url='https://t.me/movieshub_group'),
        InlineKeyboardButton('𝔖𝔬𝔲𝔯𝔠𝔢 ℭ𝔬𝔡𝔢📃', url='https://t.me/NOKIERUNNOIPPKITTUM')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Mo_tech_mrk_yt.send_message(
        chat_id=message.chat.id,
        text="""<b>👋Hey,
        
ഞാൻ <a href="https://t.me/movieshub_group">Movies Hub | മൂവീസ് ഹബ്</a> എന്ന ഗ്രൂപ്പിൽ Use Cheyan Vendi Indakiya😌 <a href="https://cnpmjs.org/package/telegraph-uploader">Telegraph Uploader</a> bot ആണ് വെറുതെ നോക്കി നിന്ന്  സമയം കളയണ്ട എന്നെ Avarke യൂസ് ചെയ്യാൻ മാത്രമേ പറ്റൂ

        
Made With Love By <a href="https://t.me/movieshub_group">Movies Hub | മൂവീസ് ഹബ്</a> </b>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@Mo_tech_mrk_yt.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🏡ᕼᗝᗰᗴ', callback_data='home'),
        InlineKeyboardButton('ℭ𝔩𝔬𝔰𝔢🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚕️𝔒𝔲𝔯 ℭ𝔥𝔞𝔫𝔫𝔢𝔩⚕️', url='https://t.me/storytimeoG')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Mo_tech_mrk_yt.send_message(
        chat_id=message.chat.id,
        text="""**വെറുതെ നോക്കി നിന്ന്  സമയം കളയണ്ട എന്നെ <a href="https://t.me/movieshub_group">Movies Hub | മൂവീസ് ഹബ്</a> എന്ന ഗ്രൂപ്പിൽ Use Cheyan Vendi Ane Indakiye😌**""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@Mo_tech_mrk_yt.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)

Mo_tech_mrk_yt.run()
