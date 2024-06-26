from classes.game import Person, bcolors

magic = [{"name": "Fire Ball", "cost": 10, "dmg": 60},
         {"name": "Thunderbolt", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENNEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=========================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    print("you chose: ", index)

    if index == 0:
        dmg = player.generate_demage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, "points of damage. Enemy HP: ", enemy.get_hp())

    enemy_choice = 0
    enemy_dmg = enemy.generate_demage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg, "points of damage. Player HP: ", player.get_hp())





#print(player.generate_spell_damge(0))
#print(player.generate_spell_damge(1))