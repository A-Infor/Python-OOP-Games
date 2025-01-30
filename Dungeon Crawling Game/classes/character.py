import random

class Character:
    def __init__(self, is_human = False):
        self._is_human = is_human
        self._level    = 1
        self._health   = random.randint(1, 9)
        self._attack   = random.randint(1, 9)
        self._defense  = random.randint(1, 9)
        
        self.print_stats()
        
    def print_stats(self):
        print('\nPLAYER' if self._is_human == True else '\nENEMY')
        print(f'LIFE: {self._health}')
        print(f'LVL : {self._level}')
        print(f'ATK : {self._attack}')
        print(f'DEF : {self._defense}')
    
    def stat_decrease(self, stat, how_much):
        self._health -= how_much
    
    def stat_increase(self, stat, how_much):
        self._health += how_much
    
    def _level_up(self):
        pass