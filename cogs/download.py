import discord
from discord.ext import commands
from discord import app_commands

from os import makedirs, listdir, remove, path
import urllib.request
import zipfile

list_path = "/home/Tintin/discord_bot/NekoBot/data"

class Download(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @app_commands.command(name="download", description="Télécharge les images de ta liste dans un fichier zip.")
    async def dl_func(self, interaction: discord.Interaction) -> None:
        
        # Vérifie si la liste de l'utilisateur existe
        if not path.exists(f"{list_path}/{interaction.user.id}.txt"):
            await interaction.response.send_message("Erreur: Ta liste ne contient aucune image.")
            return

        await interaction.response.defer(ephemeral=True)
        if not path.exists(f"{list_path}/{interaction.user.id}"):
            makedirs(f"{list_path}/{interaction.user.id}")
        
        download_list = list()
        with open(f"{list_path}/{interaction.user.id}.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                download_list.append(line)
        
        error_num = 0
        for current_img, link in enumerate(download_list):
            print(f"{current_img} {link}")
            try:
                urllib.request.urlretrieve(link, f"{list_path}/{interaction.user.id}/image_{current_img}.png")
            except:
                error_num += 1
        
        if error_num == len(download_list):
            await interaction.followup.send("Impossible de télécharger les images.")
            return
        
        zip_file = zipfile.ZipFile(f"/var/www/html/images/{interaction.user.id}.zip", "w", zipfile.ZIP_DEFLATED)
        for img in listdir(f"{list_path}/{interaction.user.id}"):
            zip_file.write(f"{list_path}/{interaction.user.id}/{img}", img, zipfile.ZIP_DEFLATED)
        zip_file.close()
        
        view = discord.ui.View(timeout=None)
        url = f"http://www.culture-sympathique.fr/images/{interaction.user.id}.zip"
        view.add_item(discord.ui.Button(label="Lien vers l'archive", style=discord.ButtonStyle.link, url=url))
        await interaction.followup.send(content=f"✅ Téléchargement terminé ! {error_num} images n'ont pas pu être téléchargées.", view=view)
        
        # Suppresion des fichiers
        for num, link in enumerate(download_list):
            remove(f"{list_path}/{interaction.user.id}/image_{num}.png")
        remove(f"{list_path}/{interaction.user.id}.txt")
        
async def setup(bot):
    await bot.add_cog(Download(bot))