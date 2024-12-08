class Character:
    name = ""
    health = 100
    damage = 3
    defense = 0

    def __init__(self, name, health = 100, damage = 3, defense = 0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense


    def print_stats(self):
        print(f'-< {self.name} >-')
        print(f'Здоровя {self.health} ')
        print(f'Шкода {self.damage} ')
        print(f'Захист {self.defense} ')
        print(f'')

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)

    def attack(self, target):
        pass


