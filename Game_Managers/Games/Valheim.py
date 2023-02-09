import os

import GameBaseClass


#####################################################################################
# Configurable variables for your specific setup
#####################################################################################

bat_files = "D:/SteamLibrary/steamapps/common/Valheim dedicated server"    
valheim_log_syntax = GameBaseClass.LogSyntax("k_ESteamNetworkingConnectionState_Connected", "k_ESteamNetworkingConnectionState_None", "Net scene destroyed")

#####################################################################################
# manager object for game settings that gets passed to the Main game_manager object
#####################################################################################
    
        