import discord
from discord.ext import commands
from discord.embeds import Embed
from discord import app_commands

from pybooru import Danbooru
from random import choice
import secrets
import passwords as pswd
from var import values
from cogs.download import Posts_Button

safe = Danbooru('safebooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Safebooru(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        
    @app_commands.command(name="safeneko", description="Affiche une image depuis Safebooru.", )
    async def safeneko(self, interaction: discord.Interaction, nombre: values, tags: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"cat_ears -furry {tags}"
        errors = 0
        for _ in range(nombre):
            try:
                image = choice(safe.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
                msg = Embed(title="Recherche:", description="Une image de Neko SFW.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Safebooru - ID {image['id']}", icon_url="https://i.pinimg.com/564x/1b/8a/82/1b8a82e579861ec8a0bfac7f378e2cce.jpg")
        
                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
        
                await interaction.followup.send(embed=msg, view=view, ephemeral=False)
            except:
                errors += 1
                continue
            
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
        
async def setup(bot):
    await bot.add_cog(Safebooru(bot))