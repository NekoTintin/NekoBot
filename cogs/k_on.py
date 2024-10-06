import discord
from discord.ext import commands
from discord import app_commands

import utils.danbooru_utils as dan_utils
from var import values, nsfw_values

class K_ON(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        
    @app_commands.command(name="azu-nyan", description="Affiche une image d'Azusa Nakano (avec des oreilles de chat.)")
    async def azu(self, react: discord.Interaction, nombre: values, nsfw: bool):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image d'Azusa de K-ON!.", f"nakano_azusa cat_ears ", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        await react.followup.send(embed=result[0], view=result[1])

async def setup(bot):
    await bot.add_cog(K_ON(bot))