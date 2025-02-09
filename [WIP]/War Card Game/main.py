from classes import Card, Deck, Player, WarCardGame

human    = Player(is_computer=False)
computer = Player(is_computer=True )
deck     = Deck  (is_empty   =False)

game     = WarCardGame(human, computer, deck)

round_counter = 0
game.print_stack_sizes()

while not game.check_game_over():
    # if (input('Press ENTER to draw a card, or Q to quit')) == 'q':
    #     break
    
    round_counter += 1
    print(f'\nRound: {round_counter}')
    game.start_battle()
    game.print_stack_sizes()
print('End of the game')