import random

from .move import Move

class Player:
    
    MARK_PLAYER   = 'X'
    MARK_COMPUTER = 'O'
    
    def __init__(self, is_human):
        self.is_human = is_human
        self.marker = Player.MARK_PLAYER if is_human else Player.MARK_COMPUTER
        
    def get_move(self):
        return self.get_human_move() if self.is_human else self.get_computer_move()
    
    def get_human_move(self):
        move = Move(0) # Invalid move
        
        while not move.is_valid():
            user_input = int(input('Please enter your move (1-9): '))
            move = Move(user_input)
            
            if not move.is_valid():
                print('Invalid input. Please, enter a integer between 1 and 9.')
            
        return move
    
    def get_computer_move(self):
        valid_choice_options = list(range(1, 10))
        move = Move(random.choice(valid_choice_options))
        print('Computer move (1-9):', move.position)
        
        return move