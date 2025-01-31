import random

class Character:
    def __init__(self, name, is_human = False):
        self._name     = name.upper()
        self._is_human = is_human
        self._level    = 1
        self._health   = random.randint(1, 9)
        self._attack   = random.randint(1, 9)
        self._defense  = random.randint(1, 9)
    
    def get_stats(self):
        return {'NAME'    : self._name    ,
                'health'  : self._health  ,
                'level'   : self._level   ,
                'attack'  : self._attack  ,
                'defense' : self._defense
                }
    
    def stat_decrease(self, stat_name, how_much):
        if how_much > 0:
            stat_value = getattr(self, '_' + stat_name)
            stat_value -= how_much
            setattr(self, '_' + stat_name, stat_value if stat_value >= 0 else 0)
    
    def stat_increase(self, stat_name, how_much):
        if how_much > 0:
            stat_value = getattr(self, '_' + stat_name)
            stat_value += how_much
            setattr(self, '_' + stat_name, stat_value)
    
    def _level_up(self):
        pass