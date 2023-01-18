from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
from pybooru import Danbooru

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Princess_connect(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(name="kiaru", aliases=["Kiaru"])
    async def kiaru(self, ctx, num=1, tag=""):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
        size = 21 + len(tag)
        for _ in range(num):
            try:
                message = from_danbooru(f"karyl_(princess_connect!) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
        await search_msg.delete()
        
    @commands.command(name="helpprinconn", aliases=["helpPrinConn", "helpPrinconn"])
    async def aidePrinconn(self, ctx):
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
    message = Embed(title="<:Princess_Connect:990382542102335528> Liste des commandes pour Princess Connect", color=0xFF5700)
    
    message.add_field(name="^^kiaru [tag]", value="Affiche une image de Kiaru.", inline=True)
    
    return message
        

async def setup(bot):
    await bot.add_cog(Princess_connect(bot))
