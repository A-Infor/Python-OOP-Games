from classes  import Move, Player, Board, TicTacToeGame

# TO-DO: input('Select difficulty level:')
# TO-DO: best-of-three!

#     A human player will play against a computer player, which will select a random position.

#     If the player selected a position that is already taken, he/she loses the turn.

#     When a row,  a column, the diagonal, or the antidiagonal is full with the player's markers, the game is over and that player wins the game.

#     If the board is full but none of the players has won the game, then there is a tie.

#     When the game is over, we will ask the user if he/she would like to continue playing. We will take user input and start a new round if the player chooses to continue the game.

game = TicTacToeGame()
game.start_game()