import os

from discord.ext import commands

import passwords

version = "1.1.0"
online_message = "It's about girls, it's about neko !"
# Dictionnaire qui stocke les cogs chargés
loaded_ext = dict()

bot = commands.Bot(command_prefix="^^", help_command=None)

# Fonction pour obtenir les modules chargés
def get_modules() -> list():
    l = list()
    for filename in loaded_ext:
        if loaded_ext[filename] == True:
            l.append(filename)
    return l

@bot.command(name="modules", aliases=['mod'])
async def modules(ctx):
    message = f"Liste des modules chargés:\n"
    for mod in get_modules():
        message += f"- *{mod}*\n"
    await ctx.send(message)


# Permet de charger un module (Cog) dans ./cogs/
@bot.command()
async def load(ctx, extensions):
    await ctx.message.delete()
    bot.load_extension(f'cogs.{extensions}')
    loaded_ext[extensions] = True

# Permet de décharger un module (Cog) dans ./cogs/ 
@bot.command()
async def unload(ctx, extensions):
    await ctx.message.delete()
    bot.unload_extension(f'cogs.{extensions}')
    loaded_ext[extensions] = False
    
# Permet de recharger un module (Cog) dans ./cogs/ 
@bot.command()
async def reload(ctx, extensions):
    await ctx.message.delete()
    bot.unload_extension(f'cogs.{extensions}')
    loaded_ext[extensions] = False
    bot.load_extension(f'cogs.{extensions}')
    loaded_ext[extensions] = True

for filename in os.listdir('/home/Tintin/Desktop/NekoBot/cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(passwords.token)
