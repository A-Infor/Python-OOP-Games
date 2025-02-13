from abc import ABC, abstractmethod

class Conflict(ABC):

    @abstractmethod
    def draw_cards(self):
        #             BATTLE        |         WAR
        # AMOUNT:     1 each        |        3 each
        # ACTION: turn them face up | keep them facing down
        # RETURN:    human_card,    |    human_spoils_pile,
        #       : computer_card     | computer_spoils_pile
        pass
    
    def engage(self, human_card, computer_card, war_spoils=None):
        winner    = self.get_round_winner(human_card, computer_card)
        cards_won = self.get_cards_won   (human_card, computer_card, war_spoils)
        
        return winner, cards_won

class Battle(Conflict):
    
    def __init__(self, human, computer):
        self._human    = human
        self._computer = computer
        
        print('Battle begins!')
    
    def draw_cards(self):
        human_card    = self._human   .draw_card()
        computer_card = self._computer.draw_card()
        
        self._print_drawn_cards(human_card, computer_card)
        
        return human_card, computer_card
    
    def get_round_winner(self, human_card, computer_card):
        if   human_card.value > computer_card.value:
            return 'Human'
        elif human_card.value < computer_card.value:
            return 'Computer'
        elif human_card.value == computer_card.value:
            return 'TIE'
        else:
            print('Error! Invalid card comparison occured!')
            return None

    def _print_drawn_cards(self, human_card, computer_card):
        print('CARDS DRAWN:')
        print("\tHUMAN'S\t\t\tCOMPUTER'S", end='\n\t')
        human_card.show()
        print('', end='\t\t\t\t')
        computer_card.show()
        print()

    def get_cards_won(self, human_card, computer_card, previous_cards):
        if previous_cards:
            return [human_card, computer_card] + previous_cards
        else:
            return [human_card, computer_card]

class War(Conflict):
    
    def __init__(self):
        print('WAR begins!')
        
        human_spoils_pile, computer_spoils_pile = self.draw_cards
        
    
    def draw_cards(self):
        human_spoils_pile    = []
        computer_spoils_pile = []
        
        for i in range(3):
            human_card    = self._human   .draw_card()
            computer_card = self._computer.draw_card()
            
            human_spoils_pile   .append(   human_card)
            computer_spoils_pile.append(computer_card)
        
        print('Both previous cards are kept in the battleground.')
        print('Six more cards drawn (hidden): 🂠 🂠 🂠 ║ 🂠 🂠 🂠')        
        
        return human_spoils_pile, computer_spoils_pile
    
    # def start_war(self, cards_from_battle):
    #     self.start_battle(cards_from_war= human_cards + computer_cards + cards_from_battle)