import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy  = enemy
        
        self.play_battle()
    
    def play_battle(self):        
        for round_counter in range(1, 1000, 1):
            if self.enemy.get_stats()['health'] > 0 and self.player.get_stats()['health'] > 0:
                round_winner   = self._play_round(round_counter)
                round_counter += 1
                print(f'Round winner: {round_winner}')
            elif self.enemy.get_stats()['health'] == 0 or self.player.get_stats()['health'] == 0:
                battle_winner = self._define_winner()
                print(f'\nBattle winner: {battle_winner}')
                return
        print('\nThe battle becomes too long. The rivals can\'t keep battling anymore, and fall in the ground, exhausted.')
        
    def _play_round(self, round_number):
        (attacker, defender) = self._define_attacker_and_defender()
        attacker_attack      = attacker.get_stats()['attack']
        defender_defense     = defender.get_stats()['defense']
        damage_caused        = max(0, attacker_attack - defender_defense)
        
        print(f'\nRound {round_number} started!')
        print(f"\t{attacker.get_stats()['NAME']} attacks with {attacker_attack} points of force")
        print(f"\t{defender.get_stats()['NAME']} blocks the attack by {defender_defense} points")
        
        print(f'\tThe resulting damage is {damage_caused}')
        defender.stat_decrease('health', damage_caused)
        
        print( '\t      PLAYER\tENEMY')
        print(f"\tLIFE:   {self.player.get_stats()['health']}    \t  {self.enemy.get_stats()['health']}")
        
        return self._define_winner()
        
    def _define_attacker_and_defender(self):
        starting_character = random.randint(0, 1)
        return (self.player, self.enemy) if starting_character == 0 else (self.enemy, self.player)
    
    def _define_winner(self):
        if   0 == self.player.get_stats()['health'] == self.enemy.get_stats()['health']:
            return None
        elif self.player.get_stats()['health'] > self.enemy.get_stats()['health']:
            return 'PLAYER'
        elif self.player.get_stats()['health'] < self.enemy.get_stats()['health']:
            return 'ENEMY'
        