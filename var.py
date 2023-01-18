version = "1.4.3"
online_message = "Nya ! Ichi ni san. Nya ! Arigato !"

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