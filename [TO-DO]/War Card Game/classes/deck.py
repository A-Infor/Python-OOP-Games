# ◼️ The Deck Class

#     The instances of this class shall have one instance attribute: cards. This attribute shall be non-public and it shall contain a list of instances of the Card class (these are the cards that belong to the deck).

#     The deck shall have a property called size, which corresponds to the length of the list of cards in the deck.

#     The user of the Deck class shall be able to choose if the deck is initially empty or not when the deck instance is created.

#     The class shall have four methods: build, show, shuffle, draw, and add.

#     The build method shall build the deck by creating 52 card instances with numbers from 2 to 14 (inclusive) for each one of the four possible suits.

#     The show method shall iterate over the list of card instances and call their show method to show the description of each card.

#     The shuffle method shall shuffle the deck (the list of cards in the deck) by calling the shuffle function from the random module. (please refer to the section on import statements if you are unfamiliar with import statements).

#     The draw method shall return and remove the last card in the list of cards in the deck (this represents removing it from the top of the deck).

#     The add method shall insert a new card object to the beginning of the list of cards in the deck (this represents removing it from the bottom of the deck).