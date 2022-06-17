from random import choice

import passwords as pwrd
from discord.embeds import Embed
from discord.ext import commands
from praw import Reddit as praw2

reddit = praw2(
    # ID pour s'identifier en tant que Bot sur Reddit
    client_id = pwrd.reddit_id,
    client_secret = pwrd.reddit_secret,
    user_agent = "discord.py:Nekobot:v1.1.0(by u/tintin361yt)",
    # ID du compte Reddit
    username = "Kirlia-chan",
    password = pwrd.reddit_password,
    # Pour éviter les messages d'Async PRAW
    check_for_async = False)   

class FromReddit(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name="nekomimi", aliases=['Nekomimi'])
    async def nekomimi(self, ctx):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche sur Reddit en cours...")
        
        try:
            message = get_post("Nekomimi")
            await ctx.send(embed=message)
        except:
            await search_msg.edit(content="Erreur: la commande à plantée.")
            return
        await search_msg.delete()
        
        
    @commands.command(name="nekohentai", aliases=["Nekohentai", "nekoHentai", "NekoHentai"])
    async def nekohentai(self, ctx):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche sur Reddit en cours...")
        
        try:
            message = get_post("Nekohentai")
            await ctx.send(embed=message)
        except:
            await search_msg.edit(content="Erreur: la commande à plantée.")
            return
        await search_msg.delete()
    
    
    @commands.command(name="Nekopara", aliases=["nekopara"])
    async def nekopara(self, ctx):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche sur Reddit en cours...")
        
        try:
            message = get_post("nekoparansfw")
            await ctx.send(embed=message)
        except:
            await search_msg.edit(content="Erreur: la commande à plantée.")
            return
        await search_msg.delete()


def get_post(sub: str) -> Embed:
    subreddit = reddit.subreddit(sub)
    
    neko_list = list(subreddit.hot(limit=200))
    submission = choice(neko_list)
    color = 0xFF5700
            
    # Envoie du message Embed
    message = Embed(title=submission.title, description="", color=color)
    message.set_author(name=f"u/{submission.author}", icon_url=submission.author.icon_img)
    message.add_field(name="Lien: ", value=submission.url, inline=True)
    message.set_footer(text=f"Depuis {sub} - ID: {submission.id}", icon_url="https://www.elementaryos-fr.org/wp-content/uploads/2019/08/logo-reddit.png")
    
    message.set_image(url=submission.url)
        
        
    return message
        

def setup(bot):
    bot.add_cog(FromReddit(bot))