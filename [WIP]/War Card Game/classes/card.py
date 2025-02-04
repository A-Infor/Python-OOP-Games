from suit import Suit

class Card:
    
    value_name_dict = {11 : 'Jack' ,
                       12 : 'Queen',
                       13 : 'King' ,
                       14 : 'Ace'  }
    
    def __init__(self, value):
        self.suit  = Suit()
        self.value = value

    def show(self):
        print('Card description:', end=' ')
        if self.is_special():
            print(Card.value_name_dict[self.value], end='')
        else:
            print(self.value, end='')
        print(f'{self.suit.description}, {self.suit.symbol}')
    
    def is_special(self):
       return True if self.value >= 11 <= 14 else False