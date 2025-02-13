from .conflict import Battle

class WarCardGame:
    
    ID_TIE      = 0
    ID_HUMAN    = 1
    ID_COMPUTER = 2
    
    def __init__(self, human, computer, deck):
        self._human    = human
        self._computer = computer
        self._deck     = deck
        
        print('War Card Game')
        self.make_initial_player_stacks()
        
        round_counter = 0
        while not self.check_game_over():
            round_counter += 1
            print(f'\nRound: {round_counter}', end=' - ')
            
            battle                    = Battle(human, computer)
            human_card, computer_card = battle.draw_cards()
            winner    , cards_won     = battle.engage    (human_card, computer_card)
            self.define_winner(winner, cards_won)
            
            self.print_stack_sizes()
            
            if round_counter > 999:
                print('There were too many battles and still no winner. Both armies are exhausted and make a peace treaty.')
                break
        print('End of the game')
        
    def make_initial_player_stacks(self):
        self._deck.shuffle()
        self.make_player_stack(self._human)
        self.make_player_stack(self._computer)
    
    def make_player_stack(self, player):
        for i in range(26):
            card = self._deck.draw()
            player.add_card(card)
    
    def check_war_viability(self):
        if self._human.can_fight_war() and self._computer.can_fight_war():
            return True
        elif not self._human.can_fight_war():
            print(f"WINNER: computer, because you only have {self._human.deck.size} cards and, thus, can't fight the war.")
            return False
        elif not self._computer.can_fight_war():
            print(f"WINNER: you, because computer only have {self._computer.deck.size} cards and, thus, can't fight the war.")
            return False
        else:
            print('Error! Unclear if both players are able to fight the war.')
            return False

    def define_winner(self, winner, cards_won):
        match winner:
            case 'TIE':
                # if self.check_war_viability():
                print("It's a tie. This is ⚔️ WAR ⚔️!")
                # input()
                # self.start_war(cards_won)
                # else:
                    # print("Game over...")
            case 'Human':
                print(f'WINNER: you. (+{len(cards_won)//2} cards)')
                self.add_cards_to_player(self._human, cards_won)
            case 'Computer':
                print(f'WINNER: computer. (+{len(cards_won)//2} cards)')
                self.add_cards_to_player(self._computer, cards_won)
            case _:
                print('An error occurred! Non-valid winner ID.')
                return False
        return winner    

    def check_game_over(self):
        if self._human.has_empty_deck():
            print('GAME OVER! The computer won.')
            return True
        elif self._computer.has_empty_deck():
            print('GAME OVER! You won!')
            return True
        else:
            return False
    
    def add_cards_to_player(self, player, list_of_cards):
        for card in list_of_cards:
            player.add_card(card)
    
    def print_stack_sizes(self):
        print('STACK SIZES:')
        print("\tHUMAN'S\t\t\tCOMPUTER'S")
        print(f'\t{self._human.deck.size}\t\t\t\t{self._computer.deck.size}')