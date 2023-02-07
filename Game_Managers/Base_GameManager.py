
class GameManager:
    def __init__(self):
        self.games = game_list
        self.base_path = base_path
        self.selected_game = ""
    
    def GetGameStatus(self, game_name):
        self.selected_game = game_name
        self.games[self.selected_game]
        
        