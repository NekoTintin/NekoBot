import discord

class Posts_Button(discord.ui.View):
    
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        
    @discord.ui.button(label="Ajouter à la liste", style=discord.ButtonStyle.success, emoji="📝")
    async def add_to_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        id = interaction.user.id
        link = interaction.message.embeds[0].image.url
        
        try:
            with open(f"/home/Tintin/discord_bot/NekoBot/data/{id}.txt", "a") as file:
                file.write(f"{link}\n")    
        except:
            await interaction.response.send_message("❌ Impossible de l'ajouter à la liste...", delete_after=30, ephemeral=True)
            return
        
        await interaction.response.send_message("✅ Ajouté à ta liste !", delete_after=30, ephemeral=True)