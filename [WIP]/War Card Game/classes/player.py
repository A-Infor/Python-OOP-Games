from deck import Deck

class Player:
    
    def __init__(self):
        self.name        = None
        self.deck        = Deck(is_empty = False)
        self.is_computer = None
        
    def has_empty_deck(self):
        return (self.deck.size == 0)
    
    def draw_card(self):
        if not self.has_empty_deck():
            return self.deck.draw()
        else: return None
    
    def add_card(self, card):
        self.deck.add(card)