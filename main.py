from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#Creating Spells
fireball = Spell("Fireball", 15, 300, "Evocation")
thunderbolt = Spell("Thunderbolt", 18, 350, "Evocation")
blizzard = Spell("Blizzard", 13, 320, "Evocation")
meteor = Spell("Meteor", 35, 1000, "Evocation")
quake = Spell("Quake", 14, 140, "Evocation")
healing_word = Spell("Healing Word", 15, 400, "Divine")
healing_touch = Spell("Healing Touch", 22, 1000, "Divine")

player_spells = [fireball, thunderbolt, blizzard, meteor, healing_touch, healing_word]

# Create some Items
potion = Item("Potion of Healing", "potion", "Heals 50 HP", 600)
greater_potion = Item("Greater Potion", "potion", "Heals 100 HP", 1000)
superior_potion = Item("Superior Potion", "potion", "Heals 500 HP", 2000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 99999)
full_elixir = Item("Fill Elixir", "elixir", "Fully restores party's HP/MP", 99999)
throwing_dagger = Item("Throwing Dagger", "attack", "Deals 50 damage", 500)
oil_bomb = Item("Oil Bomb", "attack", "Deals 500 damage", 3000)

player_items = [potion, greater_potion, throwing_dagger, elixir]

player_items = [{"item": potion, "quantity": 7},
                {"item": superior_potion, "quantity": 4},
                {"item": elixir, "quantity": 3},
                {"item": full_elixir, "quantity": 2},
                {"item": throwing_dagger, "quantity": 30},
                {"item": oil_bomb, "quantity": 1}]


# Instantiate People 
player1 = Person("Silvar: ", 4000, 75, 170, 34, player_spells, player_items)
player2 = Person("Lázaro: ", 2000, 99, 150, 34, player_spells, player_items)
player3 = Person("Gwill:  ", 6000, 40, 250, 34, player_spells, player_items)

players = [player1, player2, player3]

enemy = Person("Vermelho: ", 10000, 65, 450, 25, [], [])

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print(bcolors.BOLD + bcolors.HEADER + "========================="   + bcolors.ENDC)

    print("\n\n")
    print("NAME                   HP                                 |    MP")
    for player in players:
        player.get_stats()
    print("\n")

    enemy.get_enemy_stats()
    print("\n")

    for player in players:
        player.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice) - 1
        print("you chose: ", index)
        print("\n")

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(bcolors.FAIL + "You attacked for ", dmg, "points of damage. Enemy HP: ", enemy.get_hp(), bcolors.ENDC)

        elif index == 1:
            print("\n", player.get_mp(), "/", player.get_max_mp(), " MP")
            player.choose_magic()
            magic_choice = int(input("    Choose Spell: ")) - 1
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
            item_choice = int(input("    Choose item: ")) - 1
            
            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] <= 0:
                print(bcolors.WARNING + bcolors.BOLD + "Not enough Items..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", item.prop, "points of damage" + bcolors.ENDC) 
            
            elif item.type == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " Fully restores HP/MP"+ bcolors.ENDC) 
            
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " Deals", item.prop, "points of damage" + bcolors.ENDC)
        
        else: 
            print("quit")
            quit()
    

    enemy_choice = 0
    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print(bcolors.FAIL + bcolors.BOLD + "Enemy attacks for ", enemy_dmg, "points of damage" + bcolors.ENDC)
