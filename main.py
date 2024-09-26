from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#Creating Spells
fireball = Spell("Fireball", 10, 100, "Evocation")
thunderbolt = Spell("Thunderbolt", 12, 120, "Evocation")
blizzard = Spell("Blizzard", 10, 100, "Evocation")
meteor = Spell("Meteor", 20, 200, "Evocation")
quake = Spell("Quake", 14, 140, "Evocation")
healing_word = Spell("Healing Word", 12, 120, "Divine")
healing_touch = Spell("Healing Touch", 18, 200, "Divine")

player_spells = [fireball, thunderbolt, blizzard, meteor, healing_touch, healing_word]

# Create some Items
potion = Item("Potion of Healing", "potion", "Heals 50 HP", 50)
greater_potion = Item("Greater Potion", "potion", "Heals 100 HP", 100)
superior_potion = Item("Superior Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
full_elixir = Item("Fill Elixir", "elixir", "Fully restores party's HP/MP", 9999)
throwing_dagger = Item("Throwing Dagger", "attack", "Deals 50 damage", 50)
oil_bomb = Item("Oil Bomb", "attack", "Deals 500 damage", 500)

player_items = [potion, greater_potion, throwing_dagger]


# Instantiate People 
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print(bcolors.BOLD + bcolors.HEADER + "========================="   + bcolors.ENDC)
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    print("you chose: ", index)

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.FAIL + "You attacked for ", dmg, "points of damage. Enemy HP: ", enemy.get_hp() + bcolors.ENDC)

    elif index == 1:
        print("\n", player.get_mp(), "/", player.get_max_mp(), " MP")
        player.choose_magic()
        magic_choice = int(input("Choose Spell: ")) - 1
        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print("\nNot enough MP\n")
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print("\n"+ spell.name + " deals " + str(magic_dmg) + " points of damage\n")
    
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1
        
        if item_choice == -1:
            continue

        item = player.item[item_choice]

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for", item.prop, "points of damage" + bcolors.ENDC) 

        if item.type == "attack":
#            item_dmg = player.generate_damage(item.prop)
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " Deals", item.prop, "points of damage" + bcolors.ENDC) 
    

    enemy_choice = 0
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + bcolors.BOLD + "Enemy attacks for ", enemy_dmg, "points of damage" + bcolors.ENDC)

    print("Player: " + bcolors.OKGREEN + bcolors.BOLD, str(player.get_hp()) + "/" +  str(player.get_max_hp()), "HP" + bcolors.OKBLUE + " ", str(player.get_mp()) + "/" + str(player.get_max_mp()), "MP" + bcolors.ENDC)
    print( "Enemy: " + bcolors.FAIL + bcolors.BOLD, str(enemy.get_hp()), "/",  str(enemy.get_max_hp()), "HP"  + bcolors.ENDC)
    

  




#print(player.generate_spell_damge(0))
#print(player.generate_spell_damge(1))