import discord
from discord.ext import commands
from discord.embeds import Embed
import var

class Basic(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Démarrage de NekoBot")
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=var.online_message))
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if self.bot.user.mentioned_in(message) and message.mention_everyone == False:
            await message.channel.send(f"Hey {message.author.mention}, utilise **^^help** pour afficher la liste des commandes.")
            
    # Permet de charger un cog
    @commands.command(name="load")
    async def load(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.load_extension(f"cogs.{extention}")
        var.add_module(extention)
        await ctx.send(f"Le module {extention} à bien été chargé")
        
    # Permet de décharger un cog
    @commands.command(name="unload")
    async def unload(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.unload_extension(f"cogs.{extention}")
        var.remove_module(extention)
        await ctx.send(f"Le module {extention} à bien été déchargé")
        
    # Permet de recharger un cog
    @commands.command(name="reload")
    async def reload(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.unload_extension(f"cogs.{extention}")
        await self.bot.load_extension(f"cogs.{extention}")
        await ctx.send(f"Le module {extention} à bien été rechargé")
        
    # Envoie un message avec la liste des modules chargés
    @commands.command(name="modules", aliases=['mod'])
    async def modules(self, ctx):
        message = f"Liste des modules chargés:\n"
        for mod in var.get_modules():
            message += f"- *{mod}*\n"
        await ctx.send(message)
            
    @commands.command(name="proxynekodad")
    async def proxynekodad(self, ctx):
        await ctx.message.delete()
        
        img = discord.File("/home/Tintin/discord_bot/Kiri-chan/images/proxydad.png")
        await ctx.send("Proxy's dad be like:", file=img)
        
    @commands.command(name="help")
    async def help(self, ctx):
        await ctx.message.delete()
        await ctx.send(embed=get_help())
        
        
def get_help():
    message = Embed(title=":placard: Liste des commandes", color=0x256bdb)
    
    message.add_field(name="<:Danbooru:987708663751913533> Danbooru", value="^^helpDanbooru", inline=False)
    message.add_field(name="<:Honkai:987849130967699566> Honkai Impact 3rd", value="^^helpHonkai", inline=False)
    message.add_field(name="<:Nekopara:987708723315236864> Nekopara", value="^^helpNekopara", inline=False)
    message.add_field(name="<:Princess_Connect:990382542102335528> Princess Connect", value="^^helpPrinconn", inline=False)
    message.add_field(name="<:reddit:794069835138596886> Reddit", value="^^helpReddit", inline=False)
    message.add_field(name="<:Safebooru:987708780026417212> Safebooru", value="^^helpSafebooru", inline=False)
    message.add_field(name="<:Xenoblade:987708829624070215> Xenoblade", value="^^helpXenoblade", inline=False)
    message.set_footer(text="NekoBot", icon_url="https://cdn.discordapp.com/avatars/857707035147108352/c84184eb6f2af3148579f92d05e7007f.png?size=4096")
    
    return message
    
async def setup(bot):
    await bot.add_cog(Basic(bot))