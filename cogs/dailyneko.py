import datetime as dt
from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands, tasks
from pybooru import Danbooru
from pytz import timezone

IST = timezone('Europe/Paris')
class Dailyneko(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        self.safe = Danbooru('safebooru', username="Kiri-chan27", api_key=pswd.danbooru_api)
        self.dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)
        self.neko.start()


    @tasks.loop(hours=1)
    async def neko(self):
        await self.bot.wait_until_ready()
        now = dt.datetime.now(IST)
        if now.hour == 12 or now.hour == 23:
            posts = self.safe.post_list(tags="cat_girl", limit=10000)
            post = choice(posts)

            # Envoie du message Embed
            message = Embed(title="NEKO TIME !", description="C'est l'heure de la neko du jour !!!", color=0xFF5700)
            message.add_field(name="Lien:", value=post['file_url'], inline=True)
            message.set_footer(text="Depuis Safebooru", icon_url="https://data.apksum.com/71/com.gentdev.app.safebooru/1.0.2/icon.png")
    
            message.set_image(url=post['file_url'])
        
            channel = self.bot.get_channel(986006452848169041)
            result = await channel.send(embed=message)
            await result.add_reaction("📝")
        
        
            posts_nsfw = self.dan.post_list(tags="cat_girl nude", limit=5000)
            post_nsfw = choice(posts_nsfw)
            
            # Envoie du message Embed NSFW
            message2 = Embed(title="NEKO TIME !", description="C'est l'heure de la neko du jour !!!", color=0xFF5700)
            message2.add_field(name="Lien:", value=post_nsfw['file_url'], inline=True)
            message2.set_footer(text=f"Depuis Danbooru- ID: {post_nsfw['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
    
            message2.set_image(url=post_nsfw['file_url'])
        
            channel2 = self.bot.get_channel(1015743434331521044)
            result2 = await channel2.send(embed=message2)
            await result2.add_reaction("📝")
    
async def setup(bot):
    await bot.add_cog(Dailyneko(bot))
