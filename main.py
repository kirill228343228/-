from chacter import Character

player1 = Character(name="Jonny", health=120, damage=7, defense=0)
player1.print_stats()

player2 = Character(name="Steve", health=90, damage=12, defense=0)
player2.print_stats()

player3 = Character(name="Volodia")
player3.print_stats()

player1.attack(player2)