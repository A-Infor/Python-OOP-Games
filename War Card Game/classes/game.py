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
        
    def make_initial_player_stacks(self):
        self._deck.shuffle()
        self.make_player_stack(self._human)
        self.make_player_stack(self._computer)
    
    def make_player_stack(self, player):
        for i in range(26):
            card = self._deck.draw()
            player.add_card(card)
    
    def award_prizes(self, player, list_of_cards):
        for card in list_of_cards:
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