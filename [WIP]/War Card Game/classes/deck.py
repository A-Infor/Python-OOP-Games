class Deck:
    
    def __init__(self):
        # The user of the Deck class shall be able to choose if the deck is initially empty or not when the deck instance is created.
        
        # Shall contain a list of instances of the Card class (these are the cards that belong to the deck).
        self.cards = None
        # Corresponds to the length of the list of cards in the deck.
        self.size  = None
    
    def build(self):
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
        pass
    
    def add(self):
        #     The add method shall insert a new card object to the beginning of the list of cards in the deck (this represents removing it from the bottom of the deck).
        pass