from suit import Suit

class Card:
    
    SPECIAL_CARDS = {11 : 'Jack' ,
                     12 : 'Queen',
                     13 : 'King' ,
                     14 : 'Ace'  }
    
    def __init__(self, suit, value):
        self.suit  = Suit(suit)
        self.value = value

    def show(self):
        print(f'{self.suit.symbol}', end=' ')
        if self.is_special():
            print(Card.SPECIAL_CARDS[self.value])
        else:
            print(self.value)
    
    def is_special(self):
       return True if self.value >= 11 <= 14 else False