from .board  import Board
from .player import Player

class TicTacToeGame:
    
    def __init__(self):
        print('Welcome to Tic-Tac-Toe!')
        
        self.board = Board()
        self.difficulty_level = self._set_difficulty_level()
        if self.difficulty_level != 0:
            self.run_game()
        
    def run_game(self):
        human      = Player(is_human=True)
        computer   = Player(is_human=False)
        
        self.board.print_actual_board()
        
        while True:     # Game
            while True: # Round
                human_move = human.get_move()
                self.board.submit_move(human, human_move)
                self.board.print_actual_board()
                
                if   self.board.check_is_game_over(human, human_move):
                    print('You won this round!')
                    break
                elif self.board.check_is_tie():
                    print("It's a tie!")
                    break
                else:
                    computer_move = computer.get_move()
                    self.board.submit_move(computer, computer_move)
                    self.board.print_actual_board()
                    
                    if self.board.check_is_game_over(computer, computer_move):
                        print('The computer won this round...')
                        break
            play_again = input('Would you like to play again?\nX = Yes, O = No ')
            
            match play_again:
                case 'O' | 'o':
                    print('Bye! See you later.')
                    break
                case 'X' | 'x':
                    print('Got it!')
                    self.start_new_round()
                case  _       :
                    print('Invalid reply. Please, reply only with X or O.')
                        
    def start_new_round(self):
        print('New round:')
        self.board.reset_board()
        self.board.print_actual_board()
    
    def _set_difficulty_level(self):
        while True:
            difficulty_level = int(input("""
    Enter 0 to get information on how to play,
    or start the game by entering the desired difficult level's number:
    
    \tLEVEL COMPUTER OPPONENT                    MISTAKES (TAKEN POSITIONS)
    \t1.... Totally random moves only.           Allowed, wastes a turn.
    \t2.... Random moves, only valid positions.  Not allowed.
    \t3.... Knows how to play.                   Not allowed.
    
    Your choice: """))
    
            match difficulty_level:
                case 0:
                    self._print_tutorial()
                case 1|2|3:
                    return difficulty_level
                case _:
                    print('Invalid option! Try again.')               
    
    def _print_tutorial(self):
        print('\nThe board positions are numbered exactly the same as the numpad of your keyboard:')
        self.board.print_board_mapping()
        print('To make a move, during the game, just enter the corresponding digit!')