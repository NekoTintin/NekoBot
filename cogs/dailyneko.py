import datetime as dt
from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
import discord

from pybooru import Danbooru
from pytz import timezone
import asyncio
import var

IST = timezone('Europe/Paris')

class Buttons(discord.ui.View):
    
    @discord.ui.button(label="Ajouter à la liste", style=discord.ButtonStyle.success, emoji="📝")
    async def add_to_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        id = interaction.user.id
        link = interaction.message.embeds[0].image.url
        
        try:
            with open(f"/home/Tintin/discord_bot/NekoBot/data/{id}.txt", "a") as file:
                file.write(f"{link}\n")
            message = await interaction.response.send_message("✅ Ajouté à ta liste !", delete_after=30)
        except:
            message = await interaction.response.send_message("❌ Impossible de l'ajouter à la liste...", delete_after=30)
        
    @discord.ui.button(label="Une autre !", style=discord.ButtonStyle.danger, emoji="🔁", disabled=True)
    async def repeat(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()
        
        if interaction.channel_id == 986006452848169041:
            image = choice(self.safe.post_list(tags="cat_girl", limit=10000))
        else:
            image = choice(self.dan.post_list(tags="cat_girl nude", limit=10000))
        
        channel = interaction.channel
        
        message = Embed(title=choice(var.titles_possibilities), description=choice(var.message_possibilities), color=0xFF5700)
        message.set_footer(text="Depuis Danbooru - ID: {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=200&v=4")
        message.set_image(url=image['file_url'])
        
        view = Buttons()
        view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
        await channel.send(embed=message, view=view)
        

class Dailyneko(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.safe = Danbooru('safebooru', username="Kiri-chan27", api_key=pswd.danbooru_api)
        self.dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)
        
        bot.loop.create_task(self.neko())
        #bot.loop.create_task(self.nekonsfw())
        
    async def neko(self):
        # Attends que le bot soit prêt
        await self.bot.wait_until_ready()
        now = dt.datetime.now(IST)
        channel = self.bot.get_channel(986006452848169041)
        
        image = choice(self.safe.post_list(tags="cat_girl", limit=10000))
        
        message = Embed(title=choice(var.titles_possibilities), description=choice(var.message_possibilities), color=0xFF5700)
        message.set_footer(text="Depuis Danbooru - ID: {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=200&v=4")
        message.set_image(url=image['file_url'])
        
        while not self.bot.is_closed():
            if now.hour == 12 or now.hour == 23:
                view = Buttons()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
                await channel.send(embed=message, view=view)
            await asyncio.sleep(3600)

    async def nekonsfw(self):
        await self.bot.wait_until_ready()
        now = dt.datetime.now(IST)
        channel = self.bot.get_channel(1015743434331521044)
        
        image = choice(self.dan.post_list(tags="cat_girl nude", limit=10000))
            
            # Envoie du message Embed NSFW
        message = Embed(title=choice(var.titles_possibilities), description=choice(var.message_possibilities), color=0xd97bda)
        message.set_footer(text=f"Depuis Danbooru - ID: {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=200&v=4")
        message.set_image(url=image['file_url'])
        
        while not self.bot.is_closed():
            if now.hour == 12 or now.hour == 23:
                view = Buttons()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
                await channel.send(embed=message, view=view)
            await asyncio.sleep(3600)
    
async def setup(bot):
    await bot.add_cog(Dailyneko(bot))
