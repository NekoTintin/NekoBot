import discord
from discord.ext import commands
from discord.embeds import Embed
from discord import app_commands

from os import listdir, remove, path, mkdir
import random
import urllib.request
from zipfile import ZipFile, ZIP_DEFLATED
from path import data_path, web_path
from shutil import rmtree

class Posts_Button(discord.ui.View):
    
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        
    @discord.ui.button(label="Ajouter à ta liste", style=discord.ButtonStyle.success, emoji="📝")
    async def add_to_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        id = interaction.user.id
        link = interaction.message.embeds[0].image.url
        
        try:
            if not path.exists(f"{data_path}{id}"):
                mkdir(f"{data_path}{id}")
            with open(f"{data_path}{id}/list.txt", "a") as file:
                file.write(f"{link}\n")
            return await interaction.response.send_message("✅ Ajouté à ta liste !", delete_after=15, ephemeral=True)
        except:
            return await interaction.response.send_message("❌ Impossible de l'ajouter à la liste...", delete_after=15, ephemeral=True)

class Download(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @app_commands.command(name="download", description="Télécharge les images de ta liste dans un fichier zip.")
    async def dl_func(self, react: discord.Interaction) -> None:
        
        # Vérifie si la dossier de l'utilisateur existe
        if not path.exists(f"{data_path}{react.user.id}/list.txt"):
            return await react.response.send_message("Erreur: Ta liste ne contient aucune image.", ephemeral=True)

        await react.response.defer(ephemeral=True)
        user_folder = f"{data_path}{react.user.id}"
        
        download_list = []
        with open(f"{user_folder}/list.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                download_list.append(line)
        
        error_num = 0
        for current_img, link in enumerate(download_list):
            try:
                urllib.request.urlretrieve(link, f"{user_folder}/image_{current_img}.png")
            except:
                error_num += 1
        
        if error_num == len(download_list):
            return await react.followup.send("Impossible de télécharger les images.")
        
        # Génère un nombre aléatoire pour ce fichier zip
        zip_name = random.SystemRandom().randint(100, 99999999)
        
        if path.exists(f"{web_path}{zip_name}.zip"):
            remove(f"{web_path}{zip_name}.zip")
        
        with ZipFile(f"{web_path}{zip_name}.zip", "w", ZIP_DEFLATED) as zobj:
            for img in listdir(f"{user_folder}"):
                if img == "list.txt":
                    continue
                zobj.write(f"{user_folder}/{img}", img, ZIP_DEFLATED)
        
        view = discord.ui.View(timeout=None)
        view.add_item(discord.ui.Button(label="Lien vers l'archive", style=discord.ButtonStyle.link, url=f"http://www.culture-sympathique.fr/images/{zip_name}.zip"))
        
        await react.followup.send(content="Consulte tes DM pour obtenir le lien.", ephemeral=True)
        await react.user.send(content=f"✅ Téléchargement terminé ! Nombre d'erreur(s): {error_num}. (Archive **{zip_name}**)", view=view)
        
        # Suppresion des fichiers
        rmtree(user_folder)
    
    """
    @app_commands.command(name="nekolist", description="Affiche ta liste de tes images.")
    async def nekolist(self, interaction: discord.Interaction):
        if not path.exists(f"{data_path}/{interaction.user.id}.txt"):
            return await interaction.response.send_message("Ta liste ne contient aucune image.", ephemeral=True)
            
        msg = Embed(title=f"Liste de: {interaction.user.display_name}", description="")
        msg.set_footer(text="Nekobot", icon_url=self.bot.user.display_avatar)
        with open(f"{data_path}/{interaction.user.id}.txt", "r") as file:
            lines = file.readlines()
            for num, line in enumerate(lines):
                msg.add_field(name=f"{num}.", value=f"{line}", inline=False)
                
        await interaction.response.send_message(embed=msg, ephemeral=True)
    """
        
        
async def setup(bot):
    await bot.add_cog(Download(bot))
