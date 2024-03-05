import discord
from discord.ext import commands
from discord import app_commands

import utils.danbooru_utils as dan_utils
from var import values, nsfw_values

class Honkai(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        
    @app_commands.command(name="pardofelis", description="Affiche une image de Pardofelis.")
    async def pardofelis(self, react: discord.Interaction, nombre: values, nsfw: bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Pardofelis d'Honkai Impact 3rd.", f"pardofelis_(honkai_impact) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**pardofelis_(honkai_impact)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])

async def setup(bot):
    await bot.add_cog(Honkai(bot))
