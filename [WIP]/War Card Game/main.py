from classes import Card, Deck, Player, WarCardGame, Conflict, Battle, War

human    = Player(is_computer=False)
computer = Player(is_computer=True )
deck     = Deck  (is_empty   =False)

game     = WarCardGame(human, computer, deck)
game.make_initial_player_stacks()

round_counter = 0
while not game.check_game_over():
    round_counter += 1
    print(f'\nRound: {round_counter}', end=' - ')
    
    battle                    = Battle(human, computer)
    human_card, computer_card = battle.draw_duel_cards()
    winner    , prize         = battle.engage(human_card, computer_card)
    if (winner == human or winner == computer):
        game.award_prizes(winner, prize)
    elif winner == 'TIE':
        # if self.check_war_viability():
        input()
        war = War(human, computer, prize)
        human_spoils_pile, computer_spoils_pile = war.draw_spoils_piles()
        human_card       , computer_card        = war.draw_duel_cards  ()
        winner           , prize                = war.engage(human_card, computer_card, prize)
        game.award_prizes(winner, prize)
        input()
    else:
        print("Error in determining who was the last round's winner.")
        break
    
    game.print_stack_sizes()
    
    if round_counter > 999:
        print('There were too many battles and still no winner. Both armies are exhausted and make a peace treaty.')
        break
print('End of the game')