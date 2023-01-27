from typing import Literal

version = "1.6.1"
online_message = "Frites"

# Dictionnaire qui stocke les cogs chargés
loaded_ext = list()

# Fonction pour obtenir les modules chargés
def get_modules() -> list():
    l = list()
    for filename in loaded_ext:
        l.append(filename)
    return l

def add_module(name):
    loaded_ext.append(name)
    
def remove_module(name):
    loaded_ext.remove(name)
    
    
# Liste des titles pour le DailyNeko
titles_possibilities = ["NEKO TIME !", "DailyNeko en action !", "Un manque de Waifu ?", "C'est l'heure !", "Letzgongue !", "C'est Tipar !", "Oh no", "Wanna some Neko ?", "Une Neko sauvage apparaît !"]

# Liste des messages pour le DailyNeko
message_possibilities = ["Voici ta Neko du jour !", "Cette Neko est pour toi, à ce moment précis uniquement.", "C'est toujours important de combler les manques de Neko."]

# Liste des valeurs pour les commandes
values = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50]