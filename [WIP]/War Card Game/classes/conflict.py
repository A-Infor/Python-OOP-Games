from abc import ABC, abstractmethod

class Conflict(ABC):

    def __init__(self, human, computer):
        self._human    = human
        self._computer = computer    

    def draw_duel_cards(self):
        human_card    = self._human   .draw_card()
        computer_card = self._computer.draw_card()
        
        self._print_drawn_cards(human_card, computer_card)
        
        return human_card, computer_card
    
    def _print_drawn_cards(self, human_card, computer_card):
        print('CARDS DRAWN:')
        print("\tHUMAN'S\t\t\tCOMPUTER'S", end='\n\t')
        human_card.show()
        print('', end='\t\t\t\t')
        computer_card.show()
        print()
    
    def engage(self, human_card, computer_card, war_spoils=None):
        
        prize = self.get_cards_won(human_card, computer_card, war_spoils)
        
        if   human_card.value >  computer_card.value:
            print(f'WINNER: you. (+{len(prize)//2} cards)')
            return self._human   , prize
        elif human_card.value <  computer_card.value:
            print(f'WINNER: computer. (+{len(prize)//2} cards)')
            return self._computer, prize
        elif human_card.value == computer_card.value:
            print("It's a tie. This is ⚔️ WAR ⚔️!")
            return 'TIE', prize
        else:
            print('Error! Invalid card comparison occured!')
            return None, None
    
    def get_cards_won(self, human_card, computer_card, previous_cards):
        if previous_cards:
            return [human_card, computer_card] + previous_cards
        else:
            return [human_card, computer_card]

class Battle(Conflict):
    
    def __init__(self, human, computer):
        print('Battle begins!')
        super().__init__(human, computer)

class War(Conflict):
    
    def __init__(self, human, computer, prize):
        print('WAR begins!')
        super().__init__(human, computer)
        self._prize = prize
    
    def draw_spoils_pile(self):
        war_spoils_pile    = []
        
        for i in range(3):
            human_card    = self._human   .draw_card()
            computer_card = self._computer.draw_card()
            
            war_spoils_pile.append(human_card   )
            war_spoils_pile.append(computer_card)
            
        print('Both previous cards are kept in the battleground.')
        print('Six more cards drawn (hidden): 🂠 🂠 🂠 ║ 🂠 🂠 🂠')        
        
        return war_spoils_pile