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
    
    def get_move(self, board):
        # Only chooses blank cells, still at random.
        valid_choice_options = self.enumerate_empty_positions(board)
        
        move = Move(random.choice(list(valid_choice_options)))
        print('Computer move (1-9):', move.position)
        
        return move
    
    def enumerate_empty_positions(self, board):
        empty_positions_set = set()

        for position, (row, col) in board.BOARD_COORDS_MAP.items():
            if board.game_board[row][col] == board.EMPTY_CELL:
                empty_positions_set.add(int(position))

        return empty_positions_set

class PlayerComputer3(PlayerComputer):
    
    def get_move(self, board):
        # Doesn't play at random.
        
        # First, choose a direction where 3 marks can fit:
        direction = random.choice(['Vertical', 'Horizontal', 'Diagonal', 'Antidiagonal'])
        match direction:
            case 'Vertical'    :
                valid_choice_options = self.enumerate_empty_columns()
                if valid_choice_options: pass #       Play
                else                   : pass # Don't play
            case 'Horizontal'  :
                valid_choice_options = self.enumerate_empty_rows()
                if valid_choice_options: pass #       Play
                else                   : pass # Don't play
            case 'Diagonal'    :
                if self.is_diagonal_empty(): pass #       Play
                else                       : pass # Don't play
            case 'Antidiagonal':
                if self.is_antidiagonal_empty(): pass #       Play
                else                           : pass # Don't play
        
        move = None # Placeholder
        
        return move
    
    def enumerate_empty_columns(self, board):
        cols = [0, 1, 2]
        for col in cols:
            # Check if the col has all 3 lines empty:
            for row in [0, 1, 2]:
                # print(row, col)
                if board.game_board[row][col] != board.EMPTY_CELL:
                    cols.remove(col)
                    print(f'Computer says: col {col} is not empty.')
                    break
        
        return cols

    def enumerate_empty_rows(self, board):
        rows = [0, 1, 2]
        for row in rows:
            # Check if the col has all 3 lines empty:
            for col in [0, 1, 2]:
                # print(row, col)
                if board.game_board[row][col] != board.EMPTY_CELL:
                    rows.remove(row)
                    print(f'Computer says: row {row} is not empty.')
                    break
        
        return rows
    
    def is_diagonal_empty(self, board):
        return (board.game_board[2][0] == board.EMPTY_CELL
            and board.game_board[1][1] == board.EMPTY_CELL
            and board.game_board[0][2] == board.EMPTY_CELL)
    
    def is_antidiagonal_empty(self, board):
        return (board.game_board[0][0] == board.EMPTY_CELL
            and board.game_board[1][1] == board.EMPTY_CELL
            and board.game_board[2][2] == board.EMPTY_CELL)
    
game_board[2][0] == EMPTY_CELL and game_board[1][1] == EMPTY_CELL and game_board[0][2] == EMPTY_CELL