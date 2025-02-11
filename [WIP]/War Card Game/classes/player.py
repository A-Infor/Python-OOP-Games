from .deck import Deck

class Player:
    
    def __init__(self, is_computer):
        self.deck        = Deck(is_empty = True)
        self.is_computer = is_computer
        
    def has_empty_deck(self):
        return (self.deck.size == 0)
    
    def can_fight_war(self):
        return (self.deck.size > 3)
    
    def draw_card(self):
        if not self.has_empty_deck():
            return self.deck.draw()
        else: return None
    
    def add_card(self, card):
        self.deck.add(card)