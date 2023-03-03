import discord
from discord.ext import commands
from discord.embeds import Embed
from discord import app_commands

from pybooru import Danbooru
import passwords as pswd
from secrets import token_hex, SystemRandom
from var import values
from cogs.download import Posts_Button

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Xenoblade(commands.GroupCog, name="xenoblade"):
    
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.random = SystemRandom()
        super().__init__()
        
    @app_commands.command(name="nia", description="Affiche une image de Nia.", nsfw=True)
    async def nia(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"Nia_(xenoblade) {tag}"
        errors = 0
        for _ in range(nombre):
            try:
                image = self.random.choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Nia de Xenoblade Chronicles.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://i.kym-cdn.com/photos/images/original/002/308/234/14c.jpg")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view, ephemeral=False)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
            
    @app_commands.command(name="mio", description="Affiche une image de Mio.", nsfw=True)
    async def mio(self, interaction: discord.Interaction, nombre: values, tag: str = ""):
        await interaction.response.defer(ephemeral=False)
        
        complete_tag = f"mio_(xenoblade) {tag}"
        errors = 0
        for _ in range(nombre):
            try:
                image = self.random.choice(dan.post_list(tags=complete_tag, limit=5000))
                
                msg_color = discord.Color.from_str(f"#{token_hex(3)}")
                msg = Embed(title="Recherche:", description=f"Mio de Xenoblade Chronicles.", color=msg_color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Danbooru - ID {image['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
                msg.set_thumbnail(url="https://static.wikia.nocookie.net/xenoblade/images/2/2a/XC3_Mio_Launch_Celebration_Artwork.jpg/revision/latest/scale-to-width-down/1000?cb=20220729015426")

                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['file_url']))
            
                await interaction.followup.send(embed=msg, view=view, ephemeral=False)
            except:
                errors += 1
                continue
        
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Xenoblade(bot))