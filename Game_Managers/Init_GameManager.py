import os

file_path = f"{os.path.realpath(os.path.dirname(__file__))}\Games"
manager_path ="Game_Managers\GameManager.py"
manager_script = ""
import_data = ""
manager_list = []

with open (manager_path, 'w') as fp:
    fp.write(manager_script)

for game in os.scandir(file_path):
    tempName = f"{game.name.split('.')[0]}"
    import_data += f"from .Games import {tempName}\n"
    manager_list.append(f"{tempName}Manager")
    
with open (manager_path, 'w') as fp:
    fp.write(import_data)
    

