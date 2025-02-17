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

class PlayerComputer3(PlayerComputer2):
    
    def __init__(self, _):
        # Setting Computer memory:
        self._chosen_direction     = None
        self._valid_directions     = ['Diagonal', 'Antidiagonal'] # Nor ready yet: 'Vertical', 'Horizontal'
        
        self._empty_columns        = [0, 1, 2]
        self._empty_rows           = [0, 1, 2]
        self._diagonal_count       = 0
        self._antidiagonal_count   = 0
    
    def get_move(self, board):
        # Doesn't play at random.

        valid_choice_options = self.enumerate_board_empty_positions(board)
        
        if self._chosen_direction == None:
            self._chosen_direction = random.choice(self._valid_directions)
            print (f'Chosen direction: {self._chosen_direction}')
        
        match self._chosen_direction:
            case 'Vertical'    :
                empty_cols = self.enumerate_empty_columns(board)
                if empty_cols        :
                    # Choose one column if none is selected:
                    col_choice = random.choice(empty_cols)
                    # Select one empty cell of this column:
                    row_choice = random.choice([0, 1, 2])
                    # Translates coordinates:
                    cell_choice = board.BOARD_COORDS_MAP_REVERSED[(row_choice, col_choice)]
                    # Submit move:
                    move = Move(cell_choice)
                else                           : pass # Don't play
            case 'Horizontal'  :
                empty_rows = self.enumerate_empty_rows(board)
                if empty_rows        :
                    # Choose one row if none is selected:
                    row_choice = random.choice(empty_rows)
                    # Select one empty cell of this row:
                    col_choice = random.choice([0, 1, 2])
                    # Translates coordinates:
                    cell_choice = board.BOARD_COORDS_MAP_REVERSED[(row_choice, col_choice)]
                    # Submit move:
                    move = Move(cell_choice)
                else                           : pass # Don't play
            case 'Diagonal'    :
                # Update memory:
                self._diagonal_count = self.count_diagonal_or_antidiagonal_marks('DIAGONAL', board)
                print(f'Diagonal count: {self._diagonal_count}')
                
                if self._diagonal_count < 3 :
                    # Check which cells are empty:
                    cell_options       = [1, 5, 9]
                    valid_cell_options = []
                    for cell in cell_options:
                        if cell in valid_choice_options: valid_cell_options.append(cell)
                    # Select one empty cell of the diagonal:
                    cell_choice = random.choice(valid_cell_options)
                    # Submit move:
                    move = Move(cell_choice)
                else                           :
                    # Not a valid direction anymore:
                    self._valid_directions.remove('Diagonal')
            case 'Antidiagonal':
                # Update memory:
                self._antidiagonal_count = self.count_diagonal_or_antidiagonal_marks('ANTIDIAGONAL', board)
                print(f'Antidiagonal count: {self._antidiagonal_count}')
                
                if self._antidiagonal_count < 3 :
                    # Check which cells are empty:
                    cell_options = [7, 5, 3]
                    valid_cell_options = []
                    for cell in cell_options:
                        if cell in valid_choice_options: valid_cell_options.append(cell)
                    # Select one empty cell of the antidiagonal:
                    cell_choice = random.choice(valid_cell_options)
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
    
    def count_diagonal_or_antidiagonal_marks(self, diagonal_or_antidiagonal, board):
        DIAGONAL     = [board.game_board[2][0],
                        board.game_board[1][1],
                        board.game_board[0][2]]
        ANTIDIAGONAL = [board.game_board[0][0],
                        board.game_board[1][1],
                        board.game_board[2][2]]
        marks_count  = 0
        
        for cell in (DIAGONAL if diagonal_or_antidiagonal.upper == 'DIAGONAL' else ANTIDIAGONAL):
            if cell != board.EMPTY_CELL: marks_count += 1
        
        return marks_count