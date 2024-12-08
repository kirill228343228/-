from Character import character

player1 = character(name="Jonny", health=120, damage=7, defense=0)
player1.print_stats()

player2 = character(name="Steve", health=90, damage=12, defense=0)
player2.print_stats()

player3 = character(name="Volodia")
player3.print_stats()

player1.attack(player2)
