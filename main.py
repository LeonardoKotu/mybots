
"""
Основная задача:
Бот медиа должен отследовать сообщении, и заодно создавать ветки.
UPD: можно реакции добавлять, Погнали!

"""

import disnake
from disnake import guild
from disnake.ext import commands

intents = disnake.Intents().all() # для бота

# создание бота
bot = commands.InteractionBot(intents=intents)

#inter = disnake.Interaction

@bot.event
async def on_message(message: disnake.Message):
    #channel = disnake.utils.get(bot.get_all_channels(), name='├💞・милашки')
    cutie = bot.get_channel(1102004191255343104)
    media = bot.get_channel(1102004091795804271)
    photos = bot.get_channel(1102004345844801546)

    channels = [cutie, media, photos]

    if message.channel in channels:
        if message.attachments:
           await message.create_thread(name=f"Веточка", auto_archive_duration=10080)

@bot.slash_command()
async def tesst(ctx):
    await ctx.send("It's ok.")
bot.run("MTEwMjk0MjIwNTEyOTI2OTM5OQ.GGM0Rm.tdvqIwlUjiVIrHSypx-L-4NfxhjsqYby_gJttU")
