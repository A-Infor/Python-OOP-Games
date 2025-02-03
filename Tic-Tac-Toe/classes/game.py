from .board  import Board
from .player import Player

class TicTacToeGame:
    
    def start_game(self):
        print('Welcome to Tic-Tac-Toe')
        
        board    = Board()
        human    = Player(is_human=True)
        computer = Player(is_human=False)
        
        board.print_actual_board()
        
        while True:     # Game
            while True: # Round
                human_move = human.get_move()
                board.submit_move(human, human_move)
                board.print_actual_board()
                
                if   board.check_is_game_over(human, human_move):
                    print('You won this round!')
                    break
                elif board.check_is_tie():
                    print("It's a tie!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_actual_board()
                    
                    if board.check_is_game_over(computer, computer_move):
                        print('The computer won this round...')
                        break
            play_again = input('Would you like to play again?\nX = Yes, O = No ')
            
            match play_again:
                case 'O' | 'o':
                    print('Bye! See you later.')
                    break
                case 'X' | 'x':
                    print('Got it!')
                    self.start_new_round(board)
                case  _       :
                    print('Invalid reply. Please, reply only with X or O.')
                        
    def start_new_round(self, board):
        print('New round:')
        board.reset_board()
        board.print_actual_board()