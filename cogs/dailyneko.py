import datetime as dt
from secrets import SystemRandom

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
import discord

from pybooru import Danbooru
from pytz import timezone
import asyncio
import var
from path import data_path
from os import path, mkdir

IST = timezone('Europe/Paris')

class Buttons(discord.ui.View):
    
    def __init__(self, *, timeout = None):
        self.random = SystemRandom()
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="Ajouter à ta liste", style=discord.ButtonStyle.success, emoji="📝")
    async def add_to_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        id = interaction.user.id
        link = interaction.message.embeds[0].image.url
        
        try:
            if not path.exists(f"{data_path}{id}"):
                mkdir(f"{data_path}{id}")
            with open(f"{data_path}{id}/list.txt", "a") as file:
                file.write(f"{link}\n")
            return await interaction.response.send_message("✅ Ajouté à ta liste !", delete_after=15, ephemeral=True)
        except:
            return await interaction.response.send_message("❌ Impossible de l'ajouter à la liste...", delete_after=15, ephemeral=True)
        
        
    @discord.ui.button(label="Une autre !", style=discord.ButtonStyle.danger, emoji="🔁")
    async def repeat(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()
        
        if interaction.channel_id == 986006452848169041:
            safe = Danbooru('safebooru', username="Kiri-chan27", api_key=pswd.danbooru_api)
            is_valid = False
            while is_valid == False:
                try:
                    image = self.random.choice(safe.post_list(tags="cat_girl -furry", limit=10000))
                    icon = "https://safebooru.org//samples/3249/sample_f6d42b7a58497b59d5db9205cc29703ead5f4425.jpg?3378314"
                    is_valid = True
                except:
                    asyncio.sleep(3)
                    continue
        else:
            dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)
            is_valid = False
            while is_valid == False:
                try:
                    image = self.random.choice(dan.post_list(tags="cat_girl nude", limit=10000))
                    icon = "https://avatars.githubusercontent.com/u/57931572?s=280&v=4"
                    is_valid = True
                except:
                    asyncio.sleep(3)
                    continue
        
        channel = interaction.channel
        
        message = Embed(title=self.random.choice(var.titles_possibilities), description=self.random.choice(var.message_possibilities), color=0xFF5700)
        message.set_footer(text=f"Depuis Danbooru - ID: {image['id']}", icon_url=icon)
        message.set_image(url=image['file_url'])
        
        view = Buttons()
        view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
        await channel.send(embed=message, view=view)
        

class Dailyneko(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.safe = Danbooru('safebooru', username="Kiri-chan27", api_key=pswd.danbooru_api)
        self.dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)
        self.random = SystemRandom()
        
        bot.loop.create_task(self.neko())
        bot.loop.create_task(self.nekonsfw())
        
    async def neko(self):
        # Attends que le bot soit prêt
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(986006452848169041)
        
        while not self.bot.is_closed():
            now = dt.datetime.now(IST)
            
            if now.hour == 0 or now.hour == 12:
                is_valid = False
                while is_valid == False:
                    try:
                        image = self.random.choice(self.safe.post_list(tags="cat_girl -furry", limit=10000))
                        is_valid = True
                    except:
                        continue
        
                message = Embed(title=self.random.choice(var.titles_possibilities), description=self.random.choice(var.message_possibilities), color=0xFF5700)
                message.set_footer(text=f"Depuis Safebooru - ID: {image['id']}", icon_url="https://safebooru.org//samples/3249/sample_f6d42b7a58497b59d5db9205cc29703ead5f4425.jpg?3378314")
                message.set_image(url=image['file_url'])
            
                view = Buttons()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
                await channel.send(embed=message, view=view)
            await asyncio.sleep(3600)

    async def nekonsfw(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(1015743434331521044)
        
        while not self.bot.is_closed():
            now = dt.datetime.now(IST)
            
            if now.hour == 0 or now.hour == 12:
                is_valid = False
                while is_valid == False:
                    try:
                        image = self.random.choice(self.dan.post_list(tags="cat_girl nude", limit=10000))
                        if image.get("file_url", None) != None:
                            is_valid = True
                    except:
                        continue
            
                # Envoie du message Embed NSFW
                message = Embed(title=self.random.choice(var.titles_possibilities), description=self.random.choice(var.message_possibilities), color=0xd97bda)
                message.set_footer(text=f"Depuis Danbooru - ID: {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                message.set_image(url=image['file_url'])
                
                view = Buttons()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
                await channel.send(embed=message, view=view)
            await asyncio.sleep(3600)
    
async def setup(bot):
    await bot.add_cog(Dailyneko(bot))
