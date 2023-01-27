import discord
from discord.ext import commands
from discord.embeds import Embed
from discord import app_commands

from pybooru import Danbooru
import passwords as pswd
from random import choice
import secrets
from var import values
from template import Posts_Button

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Princess_connect(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    @app_commands.command(name="kiaru", description="Affiche une image de Kiaru.")
    async def kiaru(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"karyl_(princess_connect!) {tag}"
        errors = 0
        for _ in range(nombre):
            try:
                image = choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{secrets.token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Kiaru du jeu Princess Connect!", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://static.wikia.nocookie.net/saimoe/images/c/cb/Karyl.png/revision/latest?cb=20200804180939")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view, ephemeral=False)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
        

async def setup(bot):
    await bot.add_cog(Princess_connect(bot))
