from suit import Suit

class Card:
    
    value_name_dict = {11 : 'Jack' ,
                       12 : 'Queen',
                       13 : 'King' ,
                       14 : 'Ace'  }
    
    def __init__(self):
        self.suit  = Suit()
        self.value = None

    def show(self):
        # The show method shall display the value, suit, and symbol of the suit of the card. If the card is special, this should be the written description (e.g. "Jack") instead of the value.
        pass
    
    def is_special(self):
        # The is_special method shall return True if the value of the card is greater than or equal to 11 and False otherwise.
        pass