import os

from discord.ext import commands
import discord
import asyncio
import var

import passwords
import path

version = var.version
online_message = var.online_message

# Charge les intents par défaut
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="^^", help_command=None, intents=intents)

@bot.command()
async def startup(bot):
    async with bot:
        for filename in os.listdir(path.cogs_path):
            if filename.endswith(".py") and filename != "reactions.py":
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.start(passwords.token)

# Démarre le bot
asyncio.run(startup(bot))
