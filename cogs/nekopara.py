import discord
from discord.ext import commands
from discord import app_commands

import utils.danbooru_utils as dan_utils
from var import values, nsfw_values

class Nekopara(commands.GroupCog, group_name="nekopara"):
    
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()
        
    @app_commands.command(name="vanilla", description="Affiche une image de Vanilla.", nsfw=True)
    async def vanilla(self, react: discord.Interaction, nombre: values, nsfw: bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Vanilla du jeu Nekopara.", f"vanilla_(nekopara) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**vanilla_(nekopara)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])
    
            
    @app_commands.command(name="chocola", description="Affiche une image de Chocola.", nsfw=True)
    async def chocola(self, react: discord.Interaction, nombre: values, nsfw:bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Chocola du jeu Nekopara.", f"chocola_(nekopara) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**chocola_(nekopara)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])
    
            
    @app_commands.command(name="coconut", description="Affiche une image de Coconut.", nsfw=True)
    async def coconut(self, react: discord.Interaction, nombre: values, nsfw: bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Coconut du jeu Nekopara.", f"coconut_(nekopara) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**coconut_(nekopara)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])
    
            
    @app_commands.command(name="maple", description="Affiche une image de Maple.", nsfw=True)
    async def maple(self, react: discord.Interaction, nombre: values, nsfw: bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Maple du jeu Nekopara.", f"maple_(nekopara) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**maple_(nekopara)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])
    
            
    @app_commands.command(name="cinnamon", description="Affiche une image de Cinnamon.", nsfw=True)
    async def cinnamon(self, react: discord.Interaction, nombre: values, nsfw: bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Cinnamon du jeu Nekopara.", f"cinnamon_(nekopara) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**cinnamon_(nekopara)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])
            
            
    @app_commands.command(name="azuki", description="Affiche une image de Azuki.", nsfw=True)
    async def azuki(self, react: discord.Interaction, nombre: values, nsfw: bool, tag: str = ""):
        await self.bot.wait_until_ready()
        await react.response.defer(ephemeral=False)
        
        if nsfw and not react.channel.is_nsfw():
            return await react.followup.send("Pour afficher du NSFW, mets-toi dans un salon NSFW.")
        
        try:
            result = dan_utils.search_on_danbooru("Recherche:", "Une image de Azuki du jeu Nekopara.", f"azuki_(nekopara) {tag}", nombre, nsfw_values[nsfw])
        except:
            return await react.followup.send("Aucun résultat n'a été trouvé...")
        
        if result is None:
            return await react.followup.send("Danbooru ne permet pas de faire des recherches de plus de 2 tags (**azuki_(nekopara)** est intégré de base).")
        
        await react.followup.send(embed=result[0], view=result[1])
            
async def setup(bot):
    await bot.add_cog(Nekopara(bot))
    
    