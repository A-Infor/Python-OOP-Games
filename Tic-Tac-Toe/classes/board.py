from .player import Player
from .move   import Move

class Board:
    
    EMPTY_CELL  = 0
    
    def __init__(self):
        self.reset_board()
    
    def reset_board(self):
        self.game_board = [ [Board.EMPTY_CELL,Board.EMPTY_CELL,Board.EMPTY_CELL] ,
                            [Board.EMPTY_CELL,Board.EMPTY_CELL,Board.EMPTY_CELL] ,
                            [Board.EMPTY_CELL,Board.EMPTY_CELL,Board.EMPTY_CELL] ]
    
    def print_board_mapping(self):
        print('\n| 7 | 8 | 9 |\n| 4 | 5 | 6 |\n| 1 | 2 | 3 |')
    
    def print_actual_board(self):
        for row in self.game_board:
            print('\n|', end='')
            for cell in row:
                print('   |', end='') if cell == Board.EMPTY_CELL else print(f' {cell} |', end='')
        print()

    def submit_move(self, player, move):
        row             = move.get_row()
        col             = move.get_col()
        value           = self.game_board[row][col]
        
        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print('This position is already taken. Please enter another one.')
    
    def check_is_tie(self):
        empty_counter = 0
        
        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)
            
        return empty_counter == 0
    
    def check_is_game_over(self, player, last_move):
        return (     (self._check_row          (player, last_move) )
                  or (self._check_col          (player, last_move) )
                  or (self._check_diagonal     (player           ) )
                  or (self._check_antidiagonal (player           ) )
                )
    
    def _check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]
        
        return (board_row.count(player.marker) == 3)
    
    def _check_col(self, player, last_move):
        col_index     = last_move.get_col()
        markers_count = 0
        
        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                markers_count += 1 
        
        return (markers_count == 3)
    
    def _check_diagonal(self, player):
        markers_count = 0
        
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1
        
        return (markers_count == 3)
    
    def _check_antidiagonal(self, player):
        markers_count = 0
        
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1
        
        return (markers_count == 3)