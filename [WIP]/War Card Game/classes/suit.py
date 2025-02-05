class Suit:
    
    SYMBOLS = {'♣' : 'clubs'    ,
               '♦' : 'diamonds' ,
               '♥' : 'hearts'   ,
               '♠' : 'spades'   }
    
    def __init__(self, suit):
        self.symbol      = suit
        self.description = Suit.SYMBOLS[suit]