class WarCardGame:
    
    ID_TIE      = 0
    ID_HUMAN    = 1
    ID_COMPUTER = 2
    
    def __init__(self, human, computer, deck):
        self._human   = human
        self._computer = computer
        self._deck     = deck
        
        self.make_initial_decks()
        
    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._human)
        self.make_deck(self._computer)
    
    def make_deck(self, player):
        for i in range(26):
            card = self._deck.draw()
            player.add_card(card)
    
    def start_battle(self, cards_from_war=None):
        print('Battle begins!')
        
        human_card    = self._human   .draw_card()
        computer_card = self._computer.draw_card()
        
        print('Your card:')
        human_card.show()
        print("Computer's card")
        computer_card.show()
        
        winner    = self.get_round_winner(human_card, computer_card)
        cards_won = self.get_cards_won   (human_card, computer_card, cards_from_war)
       
        match winner:
            case 0:
                print("It's a tie. This is war!")
                self.start_war(cards_won)
            case 1:
                print('You won this round!')
                self.add_cards_to_player(self._human, cards_won)
            case 2:
                print('The computer won this round.')
                self.add_cards_to_player(self._computer, cards_won)
            case _:
                print('An error occurred! Non-valid winner ID.')
                return False
        return winner
        
    def get_round_winner(self, human_card, computer_card):
        if   human_card.value > computer_card.value:
            return WarCardGame.HUMAN
        elif human_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        elif human_card.value == computer_card.value:
            return WarCardGame.TIE
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