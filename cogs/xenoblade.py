import discord
from discord.ext import commands
from discord import app_commands

import utils.danbooru_utils as dan_utils
from var import values, nsfw_values

class Xenoblade(commands.GroupCog, group_name="xenoblade"):
    
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()
    
    @app_commands.command(name="nia", description="Affiche une image de Nia.")
    async def nia(self, react: discord.Interaction, nombre: values, nsfw: bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Nia de Xenoblade Chronicles 2 et 3.", f"nia_(xenoblade) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**nia_(xenoblade)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])
            
            
    @app_commands.command(name="mio", description="Affiche une image de Mio.")
    async def mio(self, react: discord.Interaction, nombre: values, nsfw:bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Mio de Xenoblade Chronicles 3.", f"mio_(xenoblade) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**mio_(xenoblade)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])
            
            
    @app_commands.command(name="nael", description="Affiche une image de Na'el.")
    async def nael(self, react: discord.Interaction, nombre: values, nsfw: bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Na'el de Xenoblade Chronicles 3.", f"na'el_(xenoblade) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**na'el_(xenoblade)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])    
            
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Xenoblade(bot))