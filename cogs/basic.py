from turtle import title
import discord
from discord.ext import commands
from discord.embeds import Embed
import neko

class Basic(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Démarrage de NekoBot")
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=neko.online_message))
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if self.bot.user.mentioned_in(message) and message.mention_everyone == False:
            await message.channel.send(f"Hey {message.author.mention}, utilise **^^help** pour afficher la liste des commandes.")
            
    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        
        message = Embed(title=":placard: Liste des commandes", color=0x256bdb)
        message.add_field(name="^^safeneko", value="Affiche un dessin de Neko SFW.", inline=False)
        message.add_field(name="^^nekomini", value="Affiche une image depuis le subreddit r/Nekomimi.", inline=False)
        message.add_field(name="^^nekohentai", value="Affiche une image depuis le subreddit r/Nekohentai.", inline=False)
        message.add_field(name="^^nekopara", value="Affiche une image depuis le subreddit r/Nekopara.", inline=False)
        
        await ctx.send(embed=message)
    
def setup(bot):
    bot.add_cog(Basic(bot))