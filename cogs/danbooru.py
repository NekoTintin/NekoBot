import discord
from discord.ext import commands
from discord.embeds import Embed
from discord import app_commands

from pybooru import Danbooru
from random import choice
from secrets import token_hex
import passwords as pswd
from var import values
from cogs.download import Posts_Button

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class DanbooruCog(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        
    @app_commands.command(name="randomneko", description="Affiche une image de Neko depuis Danbooru")
    async def dan(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        if not interaction.channel.is_nsfw():
            return await interaction.response.send_message("Erreur: Cette commande ne fonctionne que dans un salon NSFW.", ephemeral=True)
        await interaction.response.defer(ephemeral=False)
        
        full_tag = f"cat_girl {tag}"
        errors = 0
        for _ in range(nombre):
            try:
                image = choice(dan.post_list(tags=full_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f'#{token_hex(3)}')
                msg = Embed(title="Recherche:", description="Une image de Neko depuis Danbooru.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                
                view = Posts_Button(timeout=None)
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
                
                await interaction.followup.send(embed=msg, view=view, ephemeral=False)
            except:
                errors += 1
                continue
            
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
        
async def setup(bot):
    await bot.add_cog(DanbooruCog(bot))
