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

# ◼️  Final Move

# In our current implementation of the game, if the board is almost full, there is only one move left, and the final move is the winning move, the game will show that the result was a tie.

# For example:


#     ... Previous steps.
     
#     Positions:
#     | 1 | 2 | 3 |
#     | 4 | 5 | 6 |
#     | 7 | 8 | 9 |
#     Board:
#     | X |   | X |
#     | O | X | O |
#     | O | X | O |
     
#     Please enter your move (1-9): 2
     
#     Positions:
#     | 1 | 2 | 3 |
#     | 4 | 5 | 6 |
#     | 7 | 8 | 9 |
#     Board:
#     | X | X | X |
#     | O | X | O |
#     | O | X | O |
     
#     It's a tie! 👍 Try again.


# Try to fix this by updating the code. You will need to check if the player or the computer won the game before checking if there was a tie. 