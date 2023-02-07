import os


#####################################################################################
# Configurable variables for your specific setup
#####################################################################################

variables = {
    "bat_files": "D:/SteamLibrary/steamapps/common/Valheim dedicated server"    
}


#####################################################################################
# manager object for game settings that gets passed to the Main game_manager object
#####################################################################################
class ValheimManager:
    
    def __init__(self, base_path):
        self.name = "Valheim"
        self.base_path = base_path
        self.log_files = os.path.join(base_path, "Logs/Games/Valheim")
    
    def StatusCheck(self):
        pass
        