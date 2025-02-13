from classes import Card, Deck, Player, WarCardGame, Conflict, Battle, War

human    = Player(is_computer=False)
computer = Player(is_computer=True )
deck     = Deck  (is_empty   =False)

game     = WarCardGame(human, computer, deck)