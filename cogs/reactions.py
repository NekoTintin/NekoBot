import os
import urllib.request
from random import choice
from zipfile import ZipFile
import zipfile

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
from pybooru import Danbooru
from pathlib import Path

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Reactions(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.bot.user:
            return
        
        message = reaction.message
            
        if reaction.emoji == "\N{floppy_disk}":
            embeds = message.embeds
            await message.channel.send(embed)
            for embed in embeds:
                embed_data = embed.to_dict()
                with open(f"/home/Tintin/Desktop/NekoBot/data/{user.id}.txt", "a+") as file:
                    file.write(embed_data["fields"][0]["value"])
                    file.write("\n")
           
        
    
    @commands.command(name="downloadList", aliases=["downloadlist", 'dl'])
    async def download(self, ctx):
        await ctx.message.delete()
        
        if Path(f"/home/Tintin/Desktop/NekoBot/data/{ctx.message.author.id}.txt") == False:
            await ctx.send("Erreur: Ta liste ne contient aucun lien.")
            return
        
        search_msg = await ctx.send("<a:search:944484192018903060> Téléchargement en cours...")
        
        download_list = list()
        file = open(f"/home/Tintin/Desktop/NekoBot/data/{ctx.message.author.id}.txt", 'r')
        lines = file.readlines()
        
        for line in lines:
            download_list.append(line[:-1])
            
        try:
            os.makedirs(f"/home/Tintin/Desktop/NekoBot/data/{ctx.message.author.id}")
        except:
            pass
        
        for num, link in enumerate(download_list):
            await search_msg.edit(content=f"<a:search:944484192018903060> Téléchargement en cours ({num+1} sur {len(download_list)})...")
            try:
                urllib.request.urlretrieve(link, f"/home/Tintin/Desktop/NekoBot/data/{ctx.message.author.id}/img{num}.png")
            except:
                pass
                
        zipObj = ZipFile(f"/var/www/html/images/{ctx.message.author.id}.zip", "w", zipfile.ZIP_DEFLATED)
        await search_msg.edit(content="<a:search:944484192018903060> Compression des images...")
        for image in os.listdir(f"/home/Tintin/Desktop/NekoBot/data/{ctx.message.author.id}"):
            zipObj.write(f"/home/Tintin/Desktop/NekoBot/data/{ctx.message.author.id}/{image}")
        
        zipObj.close()
        
        await search_msg.edit(content=f"http://91.174.152.111:35080/images/{ctx.message.author.id}.zip")
        
        # Suppression des fichiers
        for num, link in enumerate(download_list):
            os.remove(f"/home/Tintin/Desktop/NekoBot/data/{ctx.message.author.id}/img{num}.png")
        os.remove(f"/home/Tintin/Desktop/NekoBot/data/{ctx.message.author.id}.txt")
        
def from_danbooru(tag: str, size: int) -> Embed:
    color = 0x00314D
    
    posts = dan.post_list(tags=tag, limit=1000)
    post = choice(posts)
            
    # Envoie du message Embed
    neko = tag[:size].capitalize()
    message = Embed(title=neko, description="", color=color)
    message.add_field(name="Lien:", value=post['file_url'], inline=True)
    message.add_field(name="Info", value="La fonction repeat est encore en développement.", inline=True)
    message.set_footer(text=f"Depuis Danbooru- ID: {post['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
            
    message.set_image(url=post['file_url'])
    
    
    return message


async def setup(bot):
    await bot.add_cog(Reactions(bot))
