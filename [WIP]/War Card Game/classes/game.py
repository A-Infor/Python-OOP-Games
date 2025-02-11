from time import sleep

class WarCardGame:
    
    ID_TIE      = 0
    ID_HUMAN    = 1
    ID_COMPUTER = 2
    
    def __init__(self, human, computer, deck):
        self._human    = human
        self._computer = computer
        self._deck     = deck
        
        print('War Card Game')
        self.make_initial_decks()
        
    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_player_stack(self._human)
        self.make_player_stack(self._computer)
    
    def make_player_stack(self, player):
        for i in range(26):
            card = self._deck.draw()
            player.add_card(card)
    
    def start_battle(self, cards_from_war=None):
        print('Battle begins!')
        
        human_card    = self._human   .draw_card()
        computer_card = self._computer.draw_card()
        
        print('CARDS DRAWN:')
        print("\tHUMAN'S\t\t\tCOMPUTER'S", end='\n\t')
        human_card.show()
        print('', end='\t\t\t\t')
        computer_card.show()
        print()
        
        winner    = self.get_round_winner(human_card, computer_card)
        cards_won = self.get_cards_won   (human_card, computer_card, cards_from_war)
       
        match winner:
            case 0:
                if self.check_war_viability():
                    print("It's a tie. This is ⚔️ WAR ⚔️!")
                    self.start_war(cards_won)
                else:
                    print("Game over...")
            case 1:
                print(f'WINNER: you. (+{len(cards_won)//2} cards)')
                self.add_cards_to_player(self._human, cards_won)
            case 2:
                print(f'WINNER: computer. (+{len(cards_won)//2} cards)')
                self.add_cards_to_player(self._computer, cards_won)
            case _:
                print('An error occurred! Non-valid winner ID.')
                return False
        return winner
        
    def get_round_winner(self, human_card, computer_card):
        if   human_card.value > computer_card.value:
            return WarCardGame.ID_HUMAN
        elif human_card.value < computer_card.value:
            return WarCardGame.ID_COMPUTER
        elif human_card.value == computer_card.value:
            return WarCardGame.ID_TIE
        else:
            print('Error! Invalid card comparison occured!')
            return None
    
    def get_cards_won(self, human_card, computer_card, previous_cards):
        if previous_cards:
            return [human_card, computer_card] + previous_cards
        else:
            return [human_card, computer_card]
    
    def add_cards_to_player(self, player, list_of_cards):
        for card in list_of_cards:
            player.add_card(card)
    
    def start_war(self, cards_from_battle):
        human_cards    = []
        computer_cards = []
        
        for i in range(3):
            human_card    = self._human   .draw_card()
            computer_card = self._computer.draw_card()
            
            human_cards   .append(   human_card)
            computer_cards.append(computer_card)
        
        print('Both previous cards are kept in the table.')
        print('Six more cards drawn (hidden): 🂠 🂠 🂠 ║ 🂠 🂠 🂠')
        
        self.start_battle(cards_from_war= human_cards + computer_cards + cards_from_battle)
    
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
    
    def check_game_over(self):
        if self._human.has_empty_deck():
            print('GAME OVER! The computer won.')
            return True
        elif self._computer.has_empty_deck():
            print('GAME OVER! You won!')
            return True
        else:
            return False
    
    def print_stack_sizes(self):
        print('STACK SIZES:')
        print("\tHUMAN'S\t\t\tCOMPUTER'S")
        print(f'\t{self._human.deck.size}\t\t\t\t{self._computer.deck.size}')