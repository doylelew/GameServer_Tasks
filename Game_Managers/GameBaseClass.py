

class LogSyntax:
    def __init__(self, connection_message, disconnect_message, shutdown_message):
        self.connection_message = connection_message
        self.disconnect_message = disconnect_message
        self. shutdown_message = shutdown_message

class GameTemplate:
    def __init__(self, log_path, log_syntax: LogSyntax):
        self.log_path = log_path
        self.log_syntax = log_syntax
        self.serverStatus = "unkown"
        
    def checkServerStatus(self):        
        game_log_data = ''
        with open(self.log_path ,"r") as game_log:
            game_log_data = game_log.read()
        
        times_connected = game_log_data.count(self.log_syntax.connection_message)
        times_disconnected = game_log_data.count(self.log_syntax.disconnect_message)
        shutdown_called = game_log_data.count(self.log_syntax.shutdown_message)
        
        if shutdown_called > 0:
            self.serverStatus = "Disconnected"
            return
        
        if times_connected > times_disconnected:
            self.serverStatus = "Connected: Active"
            return
        
        self.serverStatus = "Connected: Idle"
        return 
        
    def getServerStatus(self):
        if self.serverStatus == "unkown":
            self.checkServerStatus()
        
        return self.serverStatus