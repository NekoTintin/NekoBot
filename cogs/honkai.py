from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
from pybooru import Danbooru

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Honkai(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(name="pardofelis", aliases=["Pardofelis", "Phyllis", "phyllis", "pardo", "Pardo"])
    async def pardo(self, ctx, num=1, tag=""):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche sur Danbooru en cours...")
        
        size = 10
        for _ in range(num):
            try:
                message = from_danbooru(f"pardofelis_(honkai_impact) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
                await result.add_reaction("🔁")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
        await search_msg.delete()
        
    @commands.command(name="Elysia", aliases=["elysia", "ellie", "Ellie", "ely", "Ely"])
    async def ely(self, ctx, num=1, tag=""):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche sur Danbooru en cours...")
        
        size = 6
        for _ in range(num):
            try:
                message = from_danbooru(f"elysia_(honkai_impact) {tag}", size)
                result = await ctx.send(embed=message)
                await result.add_reaction("📝")
                await result.add_reaction("🔁")
            except:
                await search_msg.edit(content="Erreur: la commande à plantée.")
        await search_msg.delete()

        
    @commands.command(name="helpHonkai", aliases=["helphonkai"])
    async def aideHonkai(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=get_help())
        
def from_danbooru(tag: str, size: int) -> Embed:
    color = 0x00314D
    
    posts = dan.post_list(tags=tag, limit=3000)
    post = choice(posts)
            
    # Envoie du message Embed
    neko = tag[:size].capitalize()
    message = Embed(title=neko, description="", color=color)
    message.add_field(name="Lien:", value=post['file_url'], inline=True)
    message.add_field(name="Info", value="La fonction repeat est encore en développement.", inline=True)
    message.set_footer(text=f"Depuis Danbooru- ID: {post['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
            
    message.set_image(url=post['file_url'])
    
    
    return message

def get_help():
    message = Embed(title="<:Honkai:987849130967699566> Honkai Impact 3rd", description="Vous pouvez ajouter un tag à la fin de chaque commandes.", color=0x00314D)
    
    message.add_field(name="^^pardofelis [tag]", value="Affiche une image de Pardofelis.", inline=True)
    message.add_field(name="^^elysia [tag]", value="Affiche une image d'Elysia'.", inline=True)
    
    return message
  

async def setup(bot):
    await bot.add_cog(Honkai(bot))
