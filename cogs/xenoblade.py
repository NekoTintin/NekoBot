from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
from pybooru import Danbooru

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Xenoblade(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(name="nia", aliases=["Nia"])
    async def nia(self, ctx, num=1, tag=""):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
        
        size = 13 + len(tag)
        for _ in range (num):
            try:
                message = from_danbooru(f"nia_(xenoblade) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
        await search_msg.delete()
        
        
    @commands.command(name="mio", aliases=["Mio"])
    async def mio(self, ctx, num=1, tag=""):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")

        size = 13 + len(tag)
        for _ in range (num):
            try:
                message = from_danbooru(f"mio_(xenoblade) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
        await search_msg.delete()
        
    @commands.command(name="helpxenoblade", aliases=["helpXenoblade"])
    async def aideXeno(self, ctx):
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
    message = Embed(title="<:Xenoblade:987708829624070215> Liste des commandes Xenoblade", color=0xFF5700)
    
    message.add_field(name="^^nia [tag]", value="Affiche une image de Nia.", inline=True)
    message.add_field(name="^^mio [tag]", value="Affiche une image de Mio.", inline=True)
    
    return message
        

async def setup(bot):
    await bot.add_cog(Xenoblade(bot))
