import os

################################################################
# Global Variables used in the Init
################################################################

base_path = os.path.realpath(os.path.dirname(__file__))


################################################################
# Set up a Blank Manager File
################################################################

manager_path = os.path.join(base_path,"GameManager.py")
import_data = "import os\n"

with open (manager_path, 'w') as outputfile:
    outputfile.write(import_data)


#######################################################################################
# Search the Manager Files for Game Managers and import them into 2 grups of commands
#######################################################################################

games_file_path = os.path.join(base_path, "Games")
manager_list = []
list_as_text = "\n\ngame_list={\n"

for game in os.scandir(games_file_path):
    if game.name == "__pycache__":
        continue
    tempName = f"{game.name.split('.')[0]}"
    import_data += f"from Games.{tempName} import {tempName}Manager\n"
    list_as_text += f'\t"{tempName}": {tempName}Manager(base_path),\n'

list_as_text+="\t}\n"

import_data+= "\n\nbase_path = os.path.realpath(os.path.dirname(__file__))\n"

import_data += list_as_text
    

#######################################################
# combine the data and write it to the manager file
#######################################################
    
base_data= ""
    
with open (os.path.join(base_path, "Base_GameManager.py"), 'r') as baseFile:
    base_data= baseFile.read()

import_data+= base_data

with open (manager_path, 'w') as outputfile:
    outputfile.write(import_data)


#####################################################################################
# once the GameManager class is built with proper games create GameManager object
#####################################################################################
from GameManager import GameManager                   # Game Manager import is called later to gaurentee it is created before calling it

game_manager_object = GameManager()


