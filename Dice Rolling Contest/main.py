import random

COUNTER_START = 10

class DiceGame:
    def __init__(self):
        self.player_human    = Player(is_computer = False)
        self.player_computer = Player(is_computer = True )
    
    def play_game(self):
        round_number = 0
        
        print('Game started!')
        print( '               Human\tComputer')
        print(f'Counter       : {COUNTER_START}\t\t\t{COUNTER_START}')
        
        while self._is_game_over() == False:
            input('Press ENTER to roll your die (starts next round)')
            round_number += 1
            winner = self._play_round(round_number)

        print('\nGame over!')
        print(f'Game winner  : {winner}')
    
    def _play_round(self, round_number):
        print(f'\nRound {round_number}:')
        die_human    = self.player_human   .roll_die()
        die_computer = self.player_computer.roll_die()
        
        winner = self._change_counters(die_human, die_computer)
        
        print( '               Human\tComputer')
        print(f'Dice         : {die_human}\t\t\t{die_computer}')
        print(f'Counter      : {self.player_human.counter}\t\t\t{self.player_computer.counter}')
        print(f'Round winner : {winner}')
        
        return winner
        
    def _change_counters(self, die_human, die_computer):
        if die_human > die_computer:
            self.player_human   .decrement_counter()
            self.player_computer.increment_counter()
            return 'Human'
            
        elif die_computer > die_human:
            self.player_human   .increment_counter()
            self.player_computer.decrement_counter()
            return 'Computer'
        
        else:
            return 'None (tie)'
    
    def _is_game_over(self):
        return False if self.player_human.counter > 0 and self.player_computer.counter > 0 else True
        
    
class Die:
    def __init__(self):
        self._value = None
    
    def roll(self):
        self._value = random.randint(1, 6)
        return self._value

class Player:
    def __init__(self, is_computer):
        self.is_computer = is_computer
        self.counter     = COUNTER_START
        self.die         = Die()
    
    def increment_counter(self):
        self.counter += 1
        
    def decrement_counter(self):
        self.counter -= 1
        
    def roll_die(self):
        return self.die.roll()


game = DiceGame()
game.play_game ()
