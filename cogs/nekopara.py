import discord
from discord.ext import commands
from discord import app_commands
from discord.embeds import Embed

import secrets
import passwords as pswd
from pybooru import Danbooru
from random import choice
from cogs.download import Posts_Button
from var import values

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Nekopara(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        
    @app_commands.command(name="vanilla", description="Affiche une image de Vanilla.")
    async def vanilla(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"vanilla_(nekopara) {tag}"
        errors = 0
        for i in range(nombre):
            try:
                image = choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Vanilla de Nekopara.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://pbs.twimg.com/media/EHStm4yUcAAIgFe?format=png&name=small")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view, ephemeral=False)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
    
    @app_commands.command(name="chocola", description="Affiche une image de Chocola.")
    async def chocola(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"chocola_(nekopara) {tag}"
        errors = 0
        for i in range(nombre):
            try:
                image = choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Chocola de Nekopara.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://i.pinimg.com/564x/07/84/0e/07840edacdd1ab489bce6efe9ff0e599.jpg")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view, ephemeral=False)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
            
            
    @app_commands.command(name="coconut", description="Affiche une image de Coconut.")
    async def coconut(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"coconut_(nekopara) {tag}"
        errors = 0
        for i in range(nombre):
            try:
                image = choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Coconut de Nekopara.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://i.pinimg.com/564x/06/da/9d/06da9d1b176d43704a4333af04764d0c.jpg")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
    @app_commands.command(name="maple", description="Affiche une image de Maple.")
    async def maple(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"maple_(nekopara) {tag}"
        errors = 0
        for i in range(nombre):
            try:
                image = choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Maple de Nekopara.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://i.pinimg.com/564x/a1/42/4e/a1424e2e0031b38771264916f46a9368.jpg")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
    @app_commands.command(name="cinnamon", description="Affiche une image de Cinnamon.")
    async def cinnamon(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"cinnamon_(nekopara) {tag}"
        errors = 0
        for i in range(nombre):
            try:
                image = choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Cinnamon de Nekopara.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://www.nautiljon.com/images/perso/00/26/cinnamon_16162.webp?1578938713")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
    @app_commands.command(name="azuki", description="Affiche une image de Azuki.")
    async def azuki(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"azuki_(nekopara) {tag}"
        errors = 0
        for i in range(nombre):
            try:
                image = choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Azuki de Nekopara.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://wallpapercave.com/uwp/uwp1024376.jpeg")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
async def setup(bot):
    await bot.add_cog(Nekopara(bot))
    
    