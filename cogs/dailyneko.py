import discord
from discord.embeds import Embed
from discord.ext import commands

import datetime as dt
from pytz import timezone
import asyncio
from path import data_path
from os import path, mkdir
from random import SystemRandom
import requests

import passwords as pswd
import var

rating_dict = { "g": "General", "s": "Sensitive", "q": "Questionable", "e": "Explicit" }

def _create_request(tags: str) -> dict:
    headers = { "Accept": "application/json" }
    resp = requests.get("https://danbooru.donmai.us/posts/random", params=tags, headers=headers)
    
    if resp.status_code == 200:
        return resp.json()
    else:
        return None


IST = timezone('Europe/Paris')

class Buttons(discord.ui.View):
    
    def __init__(self, *, timeout = None):
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
        
        tags = {}
        if interaction.channel_id == 986006452848169041:
            tags = {"tags": "cat_ears rating:g,s"}
        else:
            tags = {"tags": "cat_ears rating:q,e"}
        
        is_valid = False
        while is_valid == False:
            try:
                image = _create_request(tags)
                is_valid = True
            except:
                asyncio.sleep(3)
                continue
        
        channel = interaction.channel
        
        message = Embed(title=SystemRandom().choice(var.titles_possibilities), description=SystemRandom().choice(var.message_possibilities), color=0xFF5700)
        message.set_footer(text=f"ID: {image['id']} - Rating {rating_dict[image['rating']]}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=200&v=4")
        message.set_image(url=image['file_url'])
        
        view = Buttons()
        view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
        await channel.send(embed=message, view=view)
        

class Dailyneko(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        #bot.loop.create_task(self._dailyneko())
        bot.loop.create_task(self._nsfwneko())
            
    async def _dailyneko(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(pswd.dailyneko_channel_id)
        
        while not self.bot.is_closed():
            now = dt.datetime.now(IST)
            
            if now.hour == 12 or now.hour == 18:
                is_valid = False
                while is_valid == False:
                    try:
                        image = _create_request({"tags": "cat_ears rating:g,s"})
                        is_valid = True
                    except:
                        continue
        
                message = Embed(title=SystemRandom().choice(var.titles_possibilities), description=SystemRandom().choice(var.message_possibilities), color=0xFF5700)
                message.set_footer(text=f"ID: {image['id']} - Rating {rating_dict[image['rating']]}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=200&v=4")
                message.set_image(url=image['file_url'])
            
                view = Buttons()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
                await channel.send(embed=message, view=view)
            await asyncio.sleep(3600)
            
    async def _nsfwneko(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(pswd.nsfwneko_channel_id)
        
        while not self.bot.is_closed():
            now = dt.datetime.now(IST)
            
            if now.hour == 0 or now.hour == 6:
                is_valid = False
                while is_valid == False:
                    try:
                        image = _create_request({"tags": "cat_ears rating:q,e"})
                        is_valid = True
                    except:
                        continue
        
                message = Embed(title=SystemRandom().choice(var.titles_possibilities), description=SystemRandom().choice(var.message_possibilities), color=0xFF5700)
                message.set_footer(text=f"ID: {image['id']} - Rating {rating_dict[image['rating']]}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=200&v=4")
                message.set_image(url=image['file_url'])
            
                view = Buttons()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
                await channel.send(embed=message, view=view)
            await asyncio.sleep(3600)
    
async def setup(bot):
    await bot.add_cog(Dailyneko(bot))
