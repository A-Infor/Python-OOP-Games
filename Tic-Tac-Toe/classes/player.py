import random
from abc import ABC, abstractmethod

from .move import Move

class Player(ABC):
    
    @abstractmethod
    def get_move(self):
        pass

class PlayerHuman(Player):
    
    MARKER = 'X'
    
    def get_move(self):
        move = Move(0) # Invalid move
        
        while not move.is_within_range():
            user_input = int(input('Please enter your move (1-9): '))
            move = Move(user_input)
            
            if not move.is_within_range():
                print('Invalid input. Please, enter a integer between 1 and 9.')
            
        return move

class PlayerComputer(Player):
    
    MARKER = 'O'
    
    def __new__(cls, difficulty_level):
        match difficulty_level:
            case 1: return object.__new__(PlayerComputer1)
            case 2: return object.__new__(PlayerComputer2)
            case 3: return object.__new__(PlayerComputer3)
            case _:
                print('Error: invalid difficulty level!')
                return False

class PlayerComputer1(PlayerComputer):
    
    def get_move(self, empty_positions_set):
        # Chooses any cell, including already filled ones.
        valid_choice_options = list(range(1, 10))
        move = Move(random.choice(valid_choice_options))
        print('Computer move (1-9):', move.position)
        
        return move

class PlayerComputer2(PlayerComputer):
    
    def get_move(self, valid_choice_options):
        # Only chooses blank cells, still at random.
        move = Move(random.choice(list(valid_choice_options)))
        print('Computer move (1-9):', move.position)
        
        return move

class PlayerComputer3(PlayerComputer):
    
    def get_move(self, valid_choice_options):
        # Doesn't play at random.
        pass