import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy  = enemy
    
    def _choose_starting_character(self):
        starting_character = random.randint(0, 1)
        return 'player' if starting_character == 0 else 'enemy'
    
    def play_battle(self):
        self._play_round()
    
    def _play_round(self):
        self._choose_starting_character()