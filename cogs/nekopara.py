from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
from pybooru import Danbooru

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Nekopara(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(name="vanilla", aliases=["Vanilla"])
    async def vanilla(self, ctx, iteration:int=1, tag=""):
        await ctx.message.delete()
        
        for _ in range (iteration):
            # Petit message d'attente
            search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
            size = 12 + len(tag)
            try:
                message = from_danbooru(f"vanilla_(nekopara) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
                if iteration == 1:
                    return
                else:
                    continue
            await search_msg.delete()
        
        
    @commands.command(name="chocola", aliases=["Chocola"])
    async def chocola(self, ctx, iteration:int=1, tag=""):
        await ctx.message.delete()
        
        for _ in range (iteration):
            # Petit message d'attente
            search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
            size = 12 + len(tag)
            try:
                message = from_danbooru(f"chocola_(nekopara) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
                if iteration == 1:
                    return
                else:
                    continue
            await search_msg.delete()
        
        
    @commands.command(name="coconut", aliases=["Coconut"])
    async def coconut(self, ctx, iteration:int=1, tag=""):
        await ctx.message.delete()
        
        for _ in range (iteration):
            # Petit message d'attente
            search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
            size = 12 + len(tag)
            try:
                message = from_danbooru(f"coconut_(nekopara) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
                if iteration == 1:
                    return
                else:
                    continue
            await search_msg.delete()
        
        
    @commands.command(name="maple", aliases=["Maple"])
    async def maple(self, ctx, iteration:int=1, tag=""):
        await ctx.message.delete()
        
        for _ in range (iteration):
            # Petit message d'attente
            search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
            size = 12 + len(tag)
            try:
                message = from_danbooru(f"maple_(nekopara) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
                if iteration == 1:
                    return
                else:
                    continue
            await search_msg.delete()
        
        
    @commands.command(name="cinnamon", aliases=["Cinnamon", "Cinna", "cinna"])
    async def cinnamon(self, ctx, iteration:int=1, tag=""):
        await ctx.message.delete()
        
        for _ in range (iteration):
            # Petit message d'attente
            search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
            size = 12 + len(tag)
            try:
                message = from_danbooru(f"cinnamon_(nekopara) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
                if iteration == 1:
                    return
                else:
                    continue
            await search_msg.delete()
        
        
    @commands.command(name="azuki", aliases=["Azuki"])
    async def azuki(self, ctx, iteration:int=1, tag=""):
        await ctx.message.delete()
        
        for _ in range (iteration):
            # Petit message d'attente
            search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
            size = 12 + len(tag)  
            try:
                message = from_danbooru(f"azuki_(nekopara) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
                if iteration == 1:
                    return
                else:
                    continue
            await search_msg.delete()
        
    
    @commands.command(name="helpNekopara", aliases=["helpnekopara"])
    async def aideNekopara(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=get_help())  
        

def from_danbooru(tag: str, size: int) -> Embed:
    color = 0x00314D
    
    posts = dan.post_list(tags=tag, limit=3000)
    post = choice(posts)
            
    # Envoie du message Embed
    neko = tag[:-size].capitalize()
    message = Embed(title=neko, description="", color=color)
    message.add_field(name="Lien:", value=post['file_url'], inline=True)
    message.set_footer(text=f"Depuis Danbooru- ID: {post['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
            
    message.set_image(url=post['file_url'])
    
    
    return message

def get_help():
    message = Embed(title="<:Nekopara:987708723315236864> Nekopara", description="Vous pouvez ajouter un tag à la fin de chaque commandes.", color=0x00314D)
    
    message.add_field(name="^^vanilla [nombre d'images] [tag]", value="Affiche une image de Vanilla.", inline=False)
    message.add_field(name="^^chocola [nombre d'images] [tag]", value="Affiche une image de Chocola.", inline=False)
    message.add_field(name="^^coconut [nombre d'images] [tag]", value="Affiche une image de Coconut.", inline=False)
    message.add_field(name="^^maple [nombre d'images] [tag]", value="Affiche une image de Maple.", inline=False)
    message.add_field(name="^^cinnamon [nombre d'images] [tag]", value="Affiche une image de Cinnamon.", inline=False)
    message.add_field(name="^^azuki [nombre d'images] [tag]", value="Affiche une image de Azuki.", inline=False)
    
    return message
  

async def setup(bot):
    await bot.add_cog(Nekopara(bot))
