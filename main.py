from classes.game import Person, bcolors
from classes.magic import Spell


fireball = Spell("Fireball", 10, 100, "Evocation")
thunderbolt = Spell("Thunderbolt", 12, 120, "Evocation")
blizzard = Spell("Blizzard", 10, 100, "Evocation")
meteor = Spell("Meteor", 20, 200, "Evocation")
quake = Spell("Quake", 14, 140, "Evocation")

healing_word = Spell("Healing Word", 12, 120, "Divine")
healing_touch = Spell("Healing Touch", 18, 200, "Divine")


# Instantiate People 
player = Person(460, 65, 60, 34, [fireball, thunderbolt, blizzard, meteor, healing_touch, healing_word])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print(bcolors.BOLD + bcolors.HEADER + "=========================")
    player.choose_action()
    choice = input("Choose Action: "  + bcolors.ENDC)
    index = int(choice) - 1
    print("you chose: ", index)

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, "points of damage. Enemy HP: ", enemy.get_hp())

    if index == 1:
        print("\n", player.get_mp(), "/", player.get_max_mp(), " MP")
        player.choose_magic()
        magic_index = int(input("Choose Spell: ")) - 1

        spell = player.magic[magic_index]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print("\nNot enough MP\n")
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print("\n"+ spell.name + " deals " + str(magic_dmg) + " points of damage\n")

    enemy_choice = 0
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg, "points of damage")

    print( "Player: ", player.get_hp(), "/",  player.get_max_hp(), " HP | ", player.get_mp(), "/", player.get_max_mp(), " MP")
    print( "Enemy: ", enemy.get_hp(), "/",  enemy.get_max_hp(), " HP")
    

  




#print(player.generate_spell_damge(0))
#print(player.generate_spell_damge(1))