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
    
    def get_move(self, _):
        # Chooses any cell, including already filled ones.
        valid_choice_options = list(range(1, 10))
        move = Move(random.choice(valid_choice_options))
        print('Computer move (1-9):', move.position)
        
        return move

class PlayerComputer2(PlayerComputer):
    
    def get_move(self, board):
        # Only chooses blank cells, still at random.
        valid_choice_options = self.enumerate_board_empty_positions(board)
        
        move = Move(random.choice(list(valid_choice_options)))
        print('Computer move (1-9):', move.position)
        
        return move
    
    def enumerate_board_empty_positions(self, board):
        empty_positions_set = set()

        for position, (row, col) in board.BOARD_COORDS_MAP.items():
            if board.game_board[row][col] == board.EMPTY_CELL:
                empty_positions_set.add(int(position))

        return empty_positions_set

class PlayerComputer3(PlayerComputer):
    
    def __init__(self, _):
        # Setting Computer memory:
        self._chosen_direction   = None
        self._valid_directions   = ['Vertical', 'Horizontal', 'Diagonal', 'Antidiagonal']
        
        self._empty_columns      = [0, 1, 2]
        self._empty_rows         = [0, 1, 2]
        self._empty_diagonal     = True
        self._empty_antidiagonal = True
    
    def get_move(self, board):
        # Doesn't play at random.
        
        if self._chosen_direction == None:
            self._chosen_direction = random.choice(self._valid_directions)
        
        match self._chosen_direction:
            case 'Vertical'    :
                valid_choice_options = self.enumerate_empty_columns(board)
                if valid_choice_options        :
                    # Choose one column if none is selected:
                    col_choice = random.choice(valid_choice_options)
                    # Select one empty cell of this column:
                    row_choice = random.choice([0, 1, 2])
                    # Translates coordinates:
                    cell_choice = board.BOARD_COORDS_MAP_REVERSED[(row_choice, col_choice)]
                    # Submit move:
                    move = Move(cell_choice)
                else                           : pass # Don't play
            case 'Horizontal'  :
                valid_choice_options = self.enumerate_empty_rows(board)
                if valid_choice_options        :
                    # Choose one row if none is selected:
                    row_choice = random.choice(valid_choice_options)
                    # Select one empty cell of this row:
                    col_choice = random.choice([0, 1, 2])
                    # Translates coordinates:
                    cell_choice = board.BOARD_COORDS_MAP_REVERSED[(row_choice, col_choice)]
                    # Submit move:
                    move = Move(cell_choice)
                else                           : pass # Don't play
            case 'Diagonal'    :
                # Update memory:
                self._empty_diagonal = self.is_diagonal_empty(board)
                
                if self._empty_diagonal    :
                    # Select one empty cell of the diagonal:
                    cell_choice = random.choice([1, 5, 9])
                    # Submit move:
                    move = Move(cell_choice)
                else                           :
                    # Not a valid direction anymore:
                    self._valid_directions.remove('Diagonal')
            case 'Antidiagonal':
                # Update memory:
                self._empty_antidiagonal = self.is_antidiagonal_empty(board)
                
                if self._empty_antidiagonal:
                    # Select one empty cell of the antidiagonal:
                    cell_choice = random.choice([7, 5, 3])
                    # Submit move:
                    move = Move(cell_choice)
                else                           :
                    # Not a valid direction anymore:
                    self._valid_directions.remove('Antidiagonal')
            case _             :
                print('Error! Invalid direction chosen.')
                return False
        
        print(f'Valid directions: {self._valid_directions}')
        return move
    
    def enumerate_empty_columns(self, board):
        cols = [0, 1, 2]
        for col in cols:
            # Check if the col has all 3 lines empty:
            for row in [0, 1, 2]:
                # print(row, col)
                if board.game_board[row][col] != board.EMPTY_CELL:
                    print(f'Computer says: col {col} is not empty. ({row},{col})')
                    cols.remove(col)
                    break
                else:
                    print(f'Computer says: col {col} is empty. ({row},{col})')
        
        return cols

    def enumerate_empty_rows(self, board):
        rows = [0, 1, 2]
        for row in rows:
            # Check if the col has all 3 lines empty:
            for col in [0, 1, 2]:
                # print(row, col)
                if board.game_board[row][col] != board.EMPTY_CELL:
                    print(f'Computer says: row {row} is not empty. ({row},{col})')
                    rows.remove(row)
                    break
                else:
                    print(f'Computer says: row {row} is empty. ({row},{col})')
        
        return rows
    
    def is_diagonal_empty(self, board):
        return (board.game_board[2][0] == board.EMPTY_CELL
            and board.game_board[1][1] == board.EMPTY_CELL
            and board.game_board[0][2] == board.EMPTY_CELL)
    
    def is_antidiagonal_empty(self, board):
        return (board.game_board[0][0] == board.EMPTY_CELL
            and board.game_board[1][1] == board.EMPTY_CELL
            and board.game_board[2][2] == board.EMPTY_CELL)