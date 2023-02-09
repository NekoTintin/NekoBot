import discord
from discord.ext import commands
from discord.embeds import Embed
from discord import app_commands

from praw import Reddit as Red
from secrets import token_hex
import passwords as pwrd
from var import values
from cogs.download import Posts_Button
from random import choice

wrapper = Red(
    # ID pour s'identifier en tant que Bot sur Reddit
    client_id = pwrd.reddit_id,
    client_secret = pwrd.reddit_secret,
    user_agent = "discord.py:Nekobot:v2.0.0(by u/tintin361yt)",
    # ID du compte Reddit
    username = "Kirlia-chan",
    password = pwrd.reddit_password,
    # Pour éviter les messages d'Async PRAW
    check_for_async = False)

class Reddit(commands.GroupCog, name="reddit"):
    
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()
        
        
    @app_commands.command(name="nekomimi", description="Affiche un post depuis r/Nekomimi.", nsfw=True)
    async def nekomimi(self, interaction: discord.Interaction, nombre: values):
        await interaction.response.defer(ephemeral=False)
        
        errors = 0
        for _ in range(nombre):
            try:
                message = get_post("Nekomimi")
                
                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers le post", style=discord.ButtonStyle.link, url=message.image.url))
                
                await interaction.followup.send(embed=message, view=view, ephemeral=False)
            except:
                errors += 1
                continue
            
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
            
    @app_commands.command(name="nekohentai", description="Affiche un post de r/Nekohentai", nsfw=True)
    async def nekohentai(self, interaction: discord.Interaction, nombre: values):
        await interaction.response.defer(ephemeral=False)
        
        errors = 0
        for _ in range(nombre):
            try:
                message = get_post("Nekohentai")
                
                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers le post", style=discord.ButtonStyle.link, url=message.image.url))
                
                await interaction.followup.send(embed=message, view=view, ephemeral=False)
            except:
                errors += 1
                continue
            
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
    
    @app_commands.command(name="nekoparansfw", description="Affiche un post de r/NekoparaNSFW", nsfw=True)
    async def nekopara(self, interaction: discord.Interaction, nombre: values):
        await interaction.response.defer(ephemeral=False)
        
        errors = 0
        for _ in range(nombre):
            try:
                message = get_post("nekoparansfw")
                
                view = Posts_Button()
                view.add_item(discord.ui.Button(label="Lien vers le post", style=discord.ButtonStyle.link, url=message.image.url))
                
                await interaction.followup.send(embed=message, view=view, ephemeral=False)
            except:
                errors += 1
                continue
            
        if errors > 0:
            await interaction.followup.send(content=f"Nombre d'images qui n'ont pas pu être affichées: {errors}.", ephemeral=True)
            
def get_post(sub: str) -> Embed:
    subreddit = wrapper.subreddit(sub)
    
    submission = choice(list(subreddit.hot(limit=650)))
    
    msg = Embed(title=submission.title, description="", color=discord.Color.from_str(f"#{token_hex(3)}"))
    msg.set_author(name=f"u/{submission.author}", icon_url=submission.author.icon_img)
    msg.set_image(url=submission.url)
    msg.set_footer(text=f"Depuis {sub} - ID: {submission.id}", icon_url="https://www.elementaryos-fr.org/wp-content/uploads/2019/08/logo-reddit.png")
    if sub == "Nekomimi":
        return msg
    msg.set_thumbnail(url=subreddit.icon_img)
    
    return msg
    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Reddit(bot))