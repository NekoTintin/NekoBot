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
        self.neko.start()


    @tasks.loop(hours=1)
    async def neko(self):
        await self.bot.wait_until_ready()
        now = dt.datetime.now(IST)
        if now.hour == 23:

            posts = self.safe.post_list(tags="cat_girl", limit=5000)
            post = choice(posts)

            # Envoie du message Embed
            message = Embed(title="NEKO TIME !", description="C'est l'heure de la neko du jour !!!", color=0xFF5700)
            message.add_field(name="Lien:", value=post['file_url'], inline=True)
            message.set_footer(text="Depuis Safebooru", icon_url="https://data.apksum.com/71/com.gentdev.app.safebooru/1.0.2/icon.png")
    
            message.set_image(url=post['file_url'])
        
            channel = self.bot.get_channel(986006452848169041)
            await channel.send(embed=message)
    
def setup(bot):
    bot.add_cog(Dailyneko(bot))
