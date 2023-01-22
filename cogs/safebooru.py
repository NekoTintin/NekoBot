import discord
from discord.ext import commands
from discord.embeds import Embed
from discord import app_commands

from pybooru import Danbooru
from random import choice
import secrets
import passwords as pswd
from template import Posts_Button

safe = Danbooru('safebooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Safebooru(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        
    @app_commands.command(name="safeneko", description="Affiche la dernière image sur Safebooru.")
    async def safeneko(self, interaction: discord.Interaction, nombre: int = 1, tags: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"cat_ears -furry {tags}"
        for _ in range(nombre):
            try:
                image = choice(safe.post_list(tags=complete_tag, limit=5000))
            except:
                continue
            
            msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
            msg = Embed(title="Recherche:", description="Une image de Neko SFW.", color=msg_color)
            msg.set_image(url=image['file_url'])
            msg.set_footer(text=f"Depuis Safebooru - ID {image['id']}", icon_url="https://danbooru.donmai.us/packs/static/images/danbooru-logo-128x128-ea111b6658173e847734.png")
        
            view = Posts_Button()
            view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
        
            await interaction.followup.send(embed=msg, view=view, ephemeral=False)
        
async def setup(bot):
    await bot.add_cog(Safebooru(bot))