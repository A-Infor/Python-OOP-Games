import random

class Character:
    def __init__(self, name, is_human = False):
        self._NAME         = name.upper()
        self._is_human     = is_human
        self._level        = 1
        self._health       = random.randint(1, 9)
        self._max_attack   = random.randint(1, 9)
        self._max_defense  = random.randint(1, 9)
    
    def get_stats(self):
        return {'NAME'        : self._NAME        ,
                'health'      : self._health      ,
                'level'       : self._level       ,
                'max_attack'  : self._max_attack  ,
                'max_defense' : self._max_defense
                }
    
    def attack(self):
        return random.randint(0, self._max_attack)
    
    def defend(self, attack_intensity):
        defense_intensity = random.randint(0, self._max_defense)
        
        damage = max(0, attack_intensity - defense_intensity)
        self.stat_decrease('health', damage)
        return defense_intensity, damage
    
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