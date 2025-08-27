COMMON = 1
UNCOMMON = 2
RARE = 3
EPIC = 4
LEGENDARY = 5

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    EPIC : RED + "E", 
    LEGENDARY : ORANGE + "L"}

class Card:
    __slots__ = ['__name', '__cost', '__rarity', '__faction', '__attack_power', '__health']


    def __init__(self, name, cost, rarity, faction, attack_power, health):
        self.__name = name
        self.__cost = cost
        self.__rarity = rarity
        self.__faction = faction
        self.__attack_power = attack_power
        self.__health = health

    
    def getName(self):
        return self.__name
    
    def getCost(self):
        return self.__cost
    
    def getRarity(self):
        return self.__rarity
    
    def getFaction(self):
        return self.__faction
    
    def getAttackPower(self):
        return self.__attack_power
    
    def getHealth(self):
        return self.__health
    
    def setHealth(self, health):
        self.__health = health

    def __repr__(self):
        return self.__name \
        + "\nRarity: " + RARITY_STRINGS[self.__rarity] \
        + "\nFaction: " + self.__faction \
        + "\nResource Cost: " + str(self.__cost) \
        + "\nAttack Power: " + str(self.__attack_power) \
        + "\nHealth Points: " + str(self.__health)
    
    def __str__(self):
        return "[" + self.__faction[0] + self.__name[0] + " " \
            + "{:02d}".format(self.__cost)+ " " \
            + "{:02d}".format(self.__attack_power) + " " \
            + "{:02d}".format(self.__health) + "]"
    
    def damage(self, amount):
        if amount > self.__health:
            extra = amount - self.__health
            self.__health = 0
            return extra
        else:
            self.__health -= amount
            return 0
        
    def is_consious(self):
        return self.__health > 0
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__rarity == other.__rarity and \
                self.__cost == other.__cost and \
                self.__faction == other.__faction and \
                self.__attack_power == other.__attack_power
        else:
            return False
        

    def __lt__(self, other):
        if type(self) == type(other):
            if self.__resource_cost != other.__resource_cost:
                return self.__resource_cost < other.__resource_cost
        else:
            raise TypeError("can't use < to compare")
        
    

    