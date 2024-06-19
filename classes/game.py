import random

class bcolors: 
    HEADER = '\033[95M'
    OKBLUE = '\033[94M'
    OKGREEN = '\033[92M'
    WARNING = '\033[93M'
    FAIL = '\033[91M'
    ENDC = '\033[0M'
    UNDERLINE = '\033[4M'
    BOLD = '\033[1M'
    
class Person: 
    
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk+10
        self.atkl = atk-10
        self.atk = atk
        self.df = df 
        self.magic = magic 
        self.actions = ["Attack", "Magic"]
        
    def generate_demage(self):
        return random.randrange(self.atkl, self.atkh)