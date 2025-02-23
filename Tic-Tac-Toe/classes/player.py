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
        self._valid_directions     = ['Vertical', 'Horizontal'] #, 'Diagonal', 'Antidiagonal']
        
        self._empty_columns        = []
        self._chosen_column        = None
        self._chosen_column_count  = 0
        
        self._empty_rows           = []
        self._chosen_row           = None
        self._chosen_row_count     = 0
        
        self._diagonal_count       =  0
        self._antidiagonal_count   =  0
    
    def get_move(self, board):
        # Doesn't play at random.
        move                 = None
        valid_choice_options = self.enumerate_board_empty_positions(board)

        while   self._valid_directions:
            if  self._chosen_direction is None:
                self._chosen_direction = random.choice(self._valid_directions)
                print (f'Chosen direction: {self._chosen_direction}')
            
            match self._chosen_direction:
                case 'Vertical'    :
                    if self._chosen_column is None:
                            self._choose_col_with_empty_cell(board, valid_choice_options)
                    else:
                        # Update memory:
                        self._chosen_column_count = self.count_vertical_or_horizontal_marks(board, 'Vertical', self._chosen_column)
                        print(f'chosen_column_count: {self._chosen_column_count}')
                        if self._chosen_column_count < 3:
                            # Select one empty cell of the chosen column:
                            row_choice = random.choice([0, 1, 2])
                            # Translates coordinates:
                            cell_choice = board.BOARD_COORDS_MAP_REVERSED[(row_choice, self._chosen_column)]
                            # Submit move:
                            move = Move(cell_choice)
                            break
                        else:
                            # Not a valid column anymore:
                            self._empty_columns.remove(self._chosen_column)
                            self._chosen_column = None
                case 'Horizontal'  :
                    if self._chosen_row is None:
                        self._choose_row_with_empty_cell(board, valid_choice_options)
                    else:
                        # Update memory:
                        self._chosen_row_count = self.count_vertical_or_horizontal_marks(board, 'Horizontal', self._chosen_row)
                        print(f'chosen_row_count: {self._chosen_row_count}')
                        if self._chosen_row_count < 3:
                            # Select one empty col of the chosen row:
                            col_choice = random.choice([0, 1, 2])
                            # Translates coordinates:
                            cell_choice = board.BOARD_COORDS_MAP_REVERSED[(self._chosen_row, col_choice)]
                            # Submit move:
                            move = Move(cell_choice)
                            break
                        else:
                            # Not a valid row anymore:
                            self._empty_rows.remove(self._chosen_row)
                            self._chosen_row = None
                case 'Diagonal'    :
                    # Update memory:
                    self._diagonal_count = self.count_diagonal_or_antidiagonal_marks('DIAGONAL', board)
                    print(f'Diagonal count: {self._diagonal_count}')
                    
                    if self._diagonal_count < 3 :
                        empty_cell_options = self._list_empty_cells(board, valid_choice_options, [1, 5, 9])
                        cell_choice        = random.choice(empty_cell_options)
                        move               = Move(cell_choice)
                        break
                    else                           :
                        # Not a valid direction anymore:
                        self._valid_directions.remove('Diagonal')
                        self._chosen_direction = None
                case 'Antidiagonal':
                    # Update memory:
                    self._antidiagonal_count = self.count_diagonal_or_antidiagonal_marks('ANTIDIAGONAL', board)
                    print(f'Antidiagonal count: {self._antidiagonal_count}')
                    
                    if self._antidiagonal_count < 3 :
                        empty_cell_options = self._list_empty_cells(board, valid_choice_options, [7, 5, 3])
                        cell_choice        = random.choice(empty_cell_options)
                        move               = Move(cell_choice)
                        break
                    else                           :
                        # Not a valid direction anymore:
                        self._valid_directions.remove('Antidiagonal')
                        self._chosen_direction = None
                case _             :
                    print('Error! Invalid direction chosen.')
                    return False
            
            print(f'Valid directions: {self._valid_directions}')
        
        return move
    
    def _choose_row_with_empty_cell(self, board, valid_choice_options):
        print('No chosen row yet!')
        
        rows = { 0 : [7, 8, 9] ,
                 1 : [4, 5, 6] ,
                 2 : [1, 2, 3] }
        
        # Checks which rows have at least 1 empty cell:
        for row_number, row_cells_list in rows.items():
            if self._list_empty_cells(board, valid_choice_options, row_cells_list): self._empty_rows.append(row_number)
        print(f'Rows with at least 1 empty cell: {self._empty_rows}')
        
        if len(self._empty_rows) > 0:
            self._chosen_row = random.choice(self._empty_rows)
            print(f'Chose row {self._chosen_row}')
        else         :
            # Not a valid direction anymore:
            self._valid_directions.remove('Horizontal')
            self._chosen_direction = None
    
    def _choose_col_with_empty_cell(self, board, valid_choice_options):
        print('No chosen column yet!')
        
        columns = { 0 : [1, 4, 7] ,
                    1 : [2, 5, 8] ,
                    2 : [3, 6, 9] }
        
        # Checks which cols have at least 1 empty cell:
        for col_number, col_cells_list in columns.items():
            if self._list_empty_cells(board, valid_choice_options, col_cells_list): self._empty_columns.append(col_number)
        print(f'Cols with at least 1 empty cell: {self._empty_columns}')
        
        if len(self._empty_columns) > 0:
            self._chosen_column = random.choice(self._empty_columns)
            print(f'Chose col {self._chosen_column}')
        else         :
            # Not a valid direction anymore:
            self._valid_directions.remove('Vertical')
            self._chosen_direction = None
    
    def _list_empty_cells(self, board, valid_choice_options, cell_options):
        
        valid_cell_options   = []
        
        for cell in cell_options:
            if cell in valid_choice_options: valid_cell_options.append(cell)
        
        return valid_cell_options
    
    def count_vertical_or_horizontal_marks(self, board, row_or_col, number):
        VERTICAL     = {0: [board.game_board[2][0], board.game_board[1][0], board.game_board[0][0]],
                        1: [board.game_board[2][1], board.game_board[1][1], board.game_board[0][1]],
                        2: [board.game_board[2][2], board.game_board[1][2], board.game_board[0][2]]}
        
        HORIZONTAL   = {0: [board.game_board[0][0], board.game_board[0][1], board.game_board[0][2]],
                        1: [board.game_board[1][0], board.game_board[1][1], board.game_board[1][2]],
                        2: [board.game_board[2][0], board.game_board[2][1], board.game_board[2][2]]}
        
        marks_count  = 0
        
        for cell in (VERTICAL[number] if row_or_col.upper() == 'VERTICAL' else HORIZONTAL[number]):
            if cell != board.EMPTY_CELL: marks_count += 1
        
        return marks_count
    
    def count_diagonal_or_antidiagonal_marks(self, diagonal_or_antidiagonal, board):
        DIAGONAL     = [board.game_board[2][0],
                        board.game_board[1][1],
                        board.game_board[0][2]]
        ANTIDIAGONAL = [board.game_board[0][0],
                        board.game_board[1][1],
                        board.game_board[2][2]]
        marks_count  = 0
        
        for cell in (DIAGONAL if diagonal_or_antidiagonal.upper() == 'DIAGONAL' else ANTIDIAGONAL):
            if cell != board.EMPTY_CELL: marks_count += 1
        
        return marks_count