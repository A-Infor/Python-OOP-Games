from classes import Character, Battle

player = Character('player', is_human=True)
enemy  = Character('enemy')

print(player.get_stats())
print(enemy.get_stats())

battle = Battle(player, enemy)