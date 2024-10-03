from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

#Creating Spells
fireball = Spell("Fireball", 15, 300, "Evocation")
thunderbolt = Spell("Thunderbolt", 18, 350, "Evocation")
blizzard = Spell("Blizzard", 13, 320, "Evocation")
meteor = Spell("Meteor", 35, 1000, "Evocation")
quake = Spell("Quake", 14, 140, "Evocation")
healing_word = Spell("Healing Word", 15, 400, "Divine")
healing_touch = Spell("Healing Touch", 22, 1000, "Divine")

player_spells = [fireball, thunderbolt, blizzard, meteor, healing_touch, healing_word]
enemy_spells = [fireball, healing_word, meteor]
# Create some Items
potion = Item("Potion of Healing", "potion", "Heals 600 HP", 600)
greater_potion = Item("Greater Potion", "potion", "Heals 1000 HP", 1000)
superior_potion = Item("Superior Potion", "potion", "Heals 2000 HP", 2000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 99999)
full_elixir = Item("Full Elixir", "elixir", "Fully restores party's HP/MP", 99999)
throwing_dagger = Item("Throwing Dagger", "attack", "Deals 500 damage", 500)
oil_bomb = Item("Oil Bomb", "attack", "Deals 3000 damage", 3000)

player_items = [potion, greater_potion, throwing_dagger, elixir]

player_items = [{"item": potion, "quantity": 7},
                {"item": superior_potion, "quantity": 4},
                {"item": elixir, "quantity": 3},
                {"item": full_elixir, "quantity": 2},
                {"item": throwing_dagger, "quantity": 30},
                {"item": oil_bomb, "quantity": 15}]


# Instantiate People 
player1 = Person("Silvar: ", 2000, 75, 170, 34, player_spells, player_items)
player2 = Person("Lázaro: ", 1000, 99, 150, 34, player_spells, player_items)
player3 = Person("Gwill:  ", 4000, 40, 250, 34, player_spells, player_items)

enemy1 = Person("Diabin   ", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Diabrete ", 10000, 65, 450, 25, enemy_spells, [])
enemy3 = Person("Diabin   ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]


running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:

    print(bcolors.BOLD + bcolors.HEADER + "=========================================================================-"   + bcolors.ENDC)
    print("NAME                   HP                                 |    MP")
    for player in players:
        player.get_stats()
    print("\n")

    for enemy in enemies:
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
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(bcolors.FAIL + "You attacked " + enemies[enemy].name + " for ", dmg, "points of damage. Enemy HP: " + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(bcolors.BOLD + bcolors.BACKGROUND + bcolors.FAIL + enemies[enemy].name + " has been defeated!" + bcolors.ENDC)
                del enemies[enemy]

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

            if spell.type == "Evocation":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print("\n"+ bcolors.BOLD + spell.name + " deals " + str(magic_dmg) + " points of damage to " + enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.BACKGROUND + bcolors.FAIL + enemies[enemy].name + " has been defeated!" + bcolors.ENDC)
                    del enemies[enemy]
            elif spell.type == "Divine": 
                player.take_damage(-magic_dmg)
                print("\n"+ bcolors.BOLD + spell.name + " heals " + str(magic_dmg) + " points of damage" + bcolors.ENDC)

        
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

                if item.name == "Full Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                        print(bcolors.OKGREEN + "\n" + item.name + " Fully restores party's HP/MP"+ bcolors.ENDC)
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " Fully restores yours HP/MP"+ bcolors.ENDC) 
            
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " Deals", item.prop, "points of damage to " + enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() <= 0:
                    print(bcolors.BOLD + bcolors.BACKGROUND + bcolors.FAIL + enemies[enemy].name + " has been defeated!" + bcolors.ENDC)
                    del enemies[enemy]

            print(bcolors.BOLD + bcolors.HEADER + "=========================================================================-"   + bcolors.ENDC)        
        else: 
            print("quit")
            quit()
    
    defeated_enemies = 0 
    defeated_players = 0

    # Condição de Vitória
    for enemy in enemies: 
        if enemy.get_hp() <= 0:
            defeated_enemies+= 1
            
    if defeated_enemies == 2:   
        print(bcolors.BACKGROUND + bcolors.BOLD + bcolors.UNDERLINE + bcolors.HEADER + "\n\nY O U     W I N !!!!!!!!!!!!!!!!!\n\n" + bcolors.ENDC)
        running = False

    # Condição de Derrota
    for player in players: 
        if player.get_hp() <= 0:
            defeated_players+= 1
        
    
    if defeated_players == 2:
        print(bcolors.BACKGROUND + bcolors.BOLD + bcolors.HEADER + "             W A S T E D            " )
        print("             X   X           " )
        print("               0              " + bcolors.ENDC)
        running = False

    # Turno do Inimigo
    for enemy in enemies:
        enemy_choice = random.randrange(0,3)
        target = random.randrange(0,len(players))
        if enemy_choice == 0:
            # Ataque
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + bcolors.BOLD + enemy.name +" attacks " + players[target].name + " for ", enemy_dmg, "points of damage" + bcolors.ENDC)
        
        elif enemy_choice == 1: 
            # Magia
            magic_choice = random.randrange(0, len(enemy.magic))
            spell = enemy.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = enemy.get_mp()
            if spell.cost > current_mp:
                print("\nNot enough MP\n")
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "Evocation":
                players[target].take_damage(magic_dmg)
                print("\n"+ enemy.name + "Conjures " + bcolors.BOLD + spell.name + " and deals " + str(magic_dmg) + " points of damage to " + players[target].name + bcolors.ENDC)
                if players[target].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.BACKGROUND + bcolors.FAIL + players[target].name + " has been WASTED!" + bcolors.ENDC)
                    del players[target]
            elif spell.type == "Divine": 
                enemy.take_damage(-magic_dmg)
                if (enemy.get_hp() > enemy.get_max_mp()):
                    enemy.mp = enemy.maxmp
                print("\n" + enemy.name + "Conjures " + bcolors.BOLD + spell.name + " and heals " + str(magic_dmg) + " points of damage" + bcolors.ENDC)
            
        elif enemy_choice == 2:
            print(enemy.name + "tentou usar um item")

