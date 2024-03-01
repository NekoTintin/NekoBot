from typing import Literal

version = "2.6.1"
online_message = "Nya Nya Nya mais genre 2.0 !"

# Dictionnaire qui stocke les cogs chargés
loaded_ext = []

# Fonction pour obtenir les modules chargés
def get_modules() -> list:
    l = list()
    for filename in loaded_ext:
        l.append(filename)
    return l

def add_module(name):
    loaded_ext.append(name)
    
def remove_module(name):
    loaded_ext.remove(name)
    
    
# Liste des titles pour le DailyNeko
titles_possibilities = ["NEKO TIME !", "DailyNeko en action !", "Un manque de Waifu ?", "C'est l'heure !", "Letzgongue !", "C'est Tipar !", "Oh no", "Une Neko sauvage apparaît !"]

# Liste des messages pour le DailyNeko
message_possibilities = ["Voici ta Neko du jour !", "C'est toujours important de combler les manques de Neko.", ]

# Liste des valeurs pour les commandes
values = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50]
nsfw_values = { True: ["explicit", "questionable"], False: ["general", "sensitive"] }

# Images pour les footer
safebooru_icon = "https://i.pinimg.com/564x/1b/8a/82/1b8a82e579861ec8a0bfac7f378e2cce.jpg"
danbooru_icon = "https://avatars.githubusercontent.com/u/57931572?s=280&v=4"