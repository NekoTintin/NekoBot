from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
from pybooru import Danbooru

safe = Danbooru('safebooru', username="Kiri-chan27", api_key=pswd.danbooru_api)


class Safebooru(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name="safeNeko", aliases=["safeneko"])
    async def random_neko(self, ctx, num=1, tag=""):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche sur Safebooru en cours...")
        
        for _ in range(num):
            try:
                message = from_danbooru(f"cat_girl {tag}", 3000)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
        await search_msg.delete()
        
    @commands.command(name="helpSafebooru", aliases=["helpsafebooru"])
    async def aideSafebooru(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=get_help())
        

def from_danbooru(tag: str, limit: int) -> Embed:
    color = 0x00314D
    
    posts = safe.post_list(tags=tag, limit=limit)
    post = choice(posts)
            
    # Envoie du message Embed
    message = Embed(title="Safeneko", description=f"", color=color)
    message.add_field(name="Lien:", value=post['file_url'], inline=True)
    message.set_footer(text=f"Depuis Safebooru - ID: {post['id']}", icon_url="https://data.apksum.com/71/com.gentdev.app.safebooru/1.0.2/icon.png")
            
    message.set_image(url=post['file_url'])
    
    
    return message


def get_help():
    message = Embed(title="<:Safebooru:987708780026417212> Liste des commandes pour Safebooru", color=0x00314D)
    
    message.add_field(name="^^safeneko [nombre d'images] [tag]", value="Affiche la dernière image sur Safebooru.", inline=True)
    
    return message
            
async def setup(bot):
    await bot.add_cog(Safebooru(bot))
