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
    
    def __init__(self, difficulty_level):
        self.intelligence = difficulty_level
    
    def get_move(self):
        match self.intelligence:
            case 1:
                return self.get_move_1()
            case 2:
                return self.get_move_2()
            case 3:
                return self.get_move_3()
            case _:
                print('Error: invalid difficulty level!')
                return False
    
    def get_move_1(self):
        # Chooses any cell, including already filled ones.
        valid_choice_options = list(range(1, 10))
        move = Move(random.choice(valid_choice_options))
        print('Computer move (1-9):', move.position)
        
        return move
    
    def get_move_2(self):
        # Only chooses blank cells, still at random.
        valid_choice_options = list(range(1, 10))
        move = Move(random.choice(valid_choice_options))
        print('Computer move (1-9):', move.position)
        
        return move
    
    def get_move_3(self):
        # Doesn't play at random.
        pass