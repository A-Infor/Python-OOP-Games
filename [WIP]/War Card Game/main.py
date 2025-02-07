from classes import Card, Deck, Player, WarCardGame

human    = Player(is_computer=False)
computer = Player(is_computer=True )
deck     = Deck  (is_empty   =False)

game     = WarCardGame(human, computer, deck)

round_counter = 0
game.print_stats ()

while not game.check_game_over():
    round_counter += 1
    print(f'\nRound: {round_counter}')
    game.start_battle()
    game.print_stats ()
    
    if (input('Press ENTER to draw another card, or Q to quit')) == 'q':
        break