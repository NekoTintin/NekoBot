from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
from pybooru import Danbooru

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class DanbooruCog(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(name="danbooru", aliases=["Danbooru", "dan", "Dan"])
    async def dan(self, ctx, iteration:int=1, tag=""):
        await ctx.message.delete()
        
        for _ in range (iteration):
            # Petit message d'attente
            search_msg = await ctx.send("<a:search:944484192018903060> Recherche sur Danbooru en cours...")
            try:
                message = from_danbooru(f"cat_girl {tag}")
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
                if iteration== 1:
                    return
                else:
                    continue
            await search_msg.delete()
        
    @commands.command(name="helpDanbooru", aliases=["helpdanbooru"])
    async def aideDanbooru(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=get_help())
        
        
def from_danbooru(tag: str) -> Embed:
    color = 0x00314D
    
    posts = dan.post_list(tags=tag, limit=3000)
    post = choice(posts)
            
    # Envoie du message Embed
    message = Embed(title="Neko !!!", description="", color=color)
    message.add_field(name="Lien:", value=post['file_url'], inline=True)
    message.set_footer(text=f"Depuis Danbooru- ID: {post['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
            
    message.set_image(url=post['file_url'])
    
    
    return message


def get_help():
    helpMSG = Embed(title="<:Danbooru:987708663751913533> Liste des commandes pour Danbooru", color=0x00314D)
    
    helpMSG.add_field(name="^^danbooru [nombre d'images] [tag]", value="Affiche une image de neko depuis Danbooru, vous pouvez ajouter un tag de recherche supplémentaire.")
    
    return helpMSG
        
async def setup(bot):
    await bot.add_cog(DanbooruCog(bot))
