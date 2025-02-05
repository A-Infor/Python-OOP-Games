import random

from card import Card

class Deck:
    
    def __init__(self, is_empty):
        self.cards = [] if is_empty else self._build()
        self.size  = len(self.cards)
            
    def _build(self):
        cards = []
        
        for suit in ['♣', '♦', '♥', '♠']:
            for value in range(2, 15):
                cards.append(Card(suit, value))
                
        return cards

    def _update_deck_size(self):
        self.size  = len(self.cards)
        
    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        card = self.cards.pop()
        self._update_deck_size()
        return card
    
    def add(self, card):
        self.cards.insert(0, card)
        self._update_deck_size()