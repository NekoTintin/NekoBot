import os

from discord.ext import commands
import discord
import asyncio
import var

import passwords

version = var.version
online_message = var.online_message
# Dictionnaire qui stocke les cogs chargés
loaded_ext = dict()

# Charge les intents par défaut
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="^^", help_command=None, intents=intents)

# Fonction pour obtenir les modules chargés
def get_modules() -> list():
    l = list()
    for filename in loaded_ext:
        if loaded_ext[filename] == True:
            l.append(filename)
    return l


        
@bot.command()
async def startup(bot):
    async with bot:
        for filename in os.listdir('/home/Tintin/discord_bot/NekoBot/cogs'):
            if filename.endswith(".py") and filename != "reactions.py":
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.start(passwords.token)

# Démarre le bot
asyncio.run(startup(bot))
