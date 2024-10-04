import random
from .magic import Spell


class bcolors: 
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BACKGROUND = '\033[40m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'


class Person:

    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk+10
        self.atkl = atk-10
        self.atk = atk
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def heal(self, dmg): 
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + " -", item)
            i += 1
    
    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.BOLD + "    TARGET: " + bcolors.ENDC)
        for enemy in enemies:
            print("        " + str(i) + "- " + enemy.name)
            i+=1
        choice = int(input("    Choose Target: ")) - 1
        return choice             



    def choose_magic(self):
        i = 1        
        print(bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("\t" + str(i) + " -" + spell.name + "(cost: " + str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1        
        print(bcolors.OKGREEN + bcolors.BOLD + "    ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("\t" + str(i) + " -", item["item"].name + ": ", item["item"].description, " (x"+str(item["quantity"])  +")")
            i += 1 

    def get_stats(self):
#        print("NAME                HP                                 | MP")
        hp_bar = self.calc_bar(25, self.maxhp, self.hp, "hp")
        mp_bar = self.calc_bar(10, self.maxmp, self.mp, "mp")
        hp_string = self.fix_string(9, str(self.hp) +"/" + str(self.maxhp))
        mp_string = self.fix_string(6, str(self.mp) +"/" + str(self.maxmp))
        print("                        _________________________           __________")
        print(bcolors.BOLD + self.name + "  "+ hp_string +"    |" + hp_bar + bcolors.BOLD +"|  " + mp_string + " |"+  mp_bar + bcolors.ENDC + "|" + bcolors.ENDC)
    
    def get_enemy_stats(self):
        
        hp_bar = self.calc_bar(70, self.maxhp, self.hp, "enemy")
        hp_string = self.fix_string(11, str(self.hp) +"/" + str(self.maxhp))
        print("                       ______________________________________________________________________")
        print(bcolors.BOLD + self.name + hp_string +"  |" + hp_bar + bcolors.BOLD +"|  " + bcolors.ENDC)

    
    def calc_bar(self, size, max, current, type):
        bar = ""
        bar_ticks = (current / max) * size

        while bar_ticks > 0:
            bar += "█"
            bar_ticks -= 1
        while len(bar) < size:
            bar += " "
        if type == "hp":
            if current < 0.25*max:
                bar = bcolors.WARNING + bar + bcolors.ENDC
            else:    
                bar = bcolors.OKGREEN + bar + bcolors.ENDC 
        elif type == "mp": 
            if current < 0.25*max:
                bar = bcolors.WARNING + bar + bcolors.ENDC
            else:    
                bar = bcolors.OKBLUE + bar + bcolors.ENDC 
        elif type == "enemy":
            if current < 0.25*max:
                bar = bcolors.WARNING + bar + bcolors.ENDC
            else:    
                bar = bcolors.BACKGROUND + bcolors.FAIL + bar + bcolors.ENDC 

        return bar
    
    def fix_string(self, size, bar_string):

        fixed_string = ""

        if len(bar_string) < size:
            diff = size - len(bar_string)
        
            while diff > 0:
                fixed_string += " "
                diff -= 1
            
            fixed_string += bar_string
        else:
            fixed_string = bar_string
        
        return fixed_string
        