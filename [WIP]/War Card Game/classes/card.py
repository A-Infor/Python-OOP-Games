class Card:
    
    SPECIAL_CARDS = {11 : 'Jack' ,
                     12 : 'Queen',
                     13 : 'King' ,
                     14 : 'Ace'  }
    
    def __init__(self, suit, value):
        self.suit  = suit
        self.value = value

    def show(self):
        print(f'{self.suit}', end=' ')
        if self.is_special(): print(Card.SPECIAL_CARDS[self.value], end='')
        else                : print(                   self.value , end='')
    
    def is_special(self):
       return True if self.value >= 11 <= 14 else False