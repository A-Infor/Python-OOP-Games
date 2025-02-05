import random

from .move import Move

class Player:
    def __init__(self):
        pass
    
    def get_move(self):
        pass

class PlayerHuman(Player):
    def __init__(self):
        self.MARKER = 'X'
    
    def get_move(self):
        move = Move(0) # Invalid move
        
        while not move.is_valid():
            user_input = int(input('Please enter your move (1-9): '))
            move = Move(user_input)
            
            if not move.is_valid():
                print('Invalid input. Please, enter a integer between 1 and 9.')
            
        return move

class PlayerComputer(Player):
    def __init__(self, difficulty_level):
        self.MARKER       = 'O'
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
        valid_choice_options = list(range(1, 10))
        move = Move(random.choice(valid_choice_options))
        print('Computer move (1-9):', move.position)
        
        return move
    
    def get_move_2(self):
        # Only chooses blank cells, still at random.
        pass
    
    def get_move_3(self):
        # Doesn't play at random.
        pass