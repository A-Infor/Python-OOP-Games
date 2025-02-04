from deck import Deck

class Player:
    
    def __init__(self):
        self.name        = None
        self.deck        = Deck()
        self.is_computer = None
        
    def has_empty_deck(self):
        # The has_empty_deck method shall return True if the size of the player's deck is 0. Else, it shall return False.
        pass
    
    def draw_card(self):
        # The draw_card method shall draw a card from the player's deck if the deck is not empty and return it.
        pass
    
    def add_card(self):
        # The add_card method shall add a card to the bottom of the player's deck. 
        pass