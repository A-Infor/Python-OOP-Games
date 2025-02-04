class Suit:
    
    symbol_description_dict = {'clubs'    : '♣',
                               'diamonds' : '♦',
                               'hearts'   : '♥',
                               'spades'   : '♠'}
    
    def __init__(self):
        self.description = None
        self.symbol      = None