import random

from card import Card

class Deck:
    
    def __init__(self):
        # The user of the Deck class shall be able to choose if the deck is initially empty or not when the deck instance is created.
        
        self.cards = []
        self.size  = len(self.cards)
    
    def _update_deck_size(self):
        self.size  = len(self.cards)
    
    def build(self):        
        for i in range(52):
            self.cards.append(Card(random.randint(2, 14)))
        self._update_deck_size()
        #     The build method shall build the deck by creating 52 card instances with numbers from 2 to 14 (inclusive) for each one of the four possible suits.
        pass
    
    def show(self):
        #     The show method shall iterate over the list of card instances and call their show method to show the description of each card.
        pass
    
    def shuffle(self):
        #     The shuffle method shall shuffle the deck (the list of cards in the deck) by calling the shuffle function from the random module. (please refer to the section on import statements if you are unfamiliar with import statements).
        pass
    
    def draw(self):
        #     The draw method shall return and remove the last card in the list of cards in the deck (this represents removing it from the top of the deck).
        self._update_deck_size()
        pass
    
    def add(self):
        #     The add method shall insert a new card object to the beginning of the list of cards in the deck (this represents removing it from the bottom of the deck).
        self._update_deck_size()
        pass