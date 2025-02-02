class Board:
    
    EMPTY_CELL = 0
    
    def __init__(self):
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

                
board = Board()
board.print_board_mapping()
board.print_actual_board()