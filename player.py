import goat_attributes

class Player:
    __slots__ = ['__name', '__score', 'resource_points', '__deck']

    def __init__(self, name, score, resource_points):
        self.__name = name
        self.__score = score
        self.__resource_points = resource_points
        self.__deck = []
        self.__hand = []
        self.__batallion = []
        self.__discarded = []
        self.__maximum_points = 0

    def getPoints(self):
        return self.__resource_points
    
    def getScore(self):
        return self.__score
    
    def getBatallion(self):
        return self.__batallion

    def __str__(self):
        """
        Returns a string in the format 'Player: <Name>"
        """
        return "Player: " + self.__name
    

    def __repr__(self):
        """
        
        """
        batallion = " "
        hand = " "
        for i in  self.__batallion:
            batallion += str(self.__batallion[i])
            batallion += ", "
        for i in self.__hand:
            hand += str(self.__hand(i))
            hand += ", "
        return self.__name + \
            "Score: " + str(self.__score) \
            + "Points: " + str(self.__resource_points) + "/10" + \
            "Deck: " + self.__deck + \
            "Batallion: " + batallion + \
            "Hand:" + hand
    
    def start_turn(self):
        """
        This method adds one resource point to the player's current resource points at the start of their turn, up to a 
        maximum of 10 resource points. Any resource points spent in the previous turn are also refunded. A card is then
        drawn from a player's deck and placed into their current hand.
        """

        self.__resource_points +=1
        if self.__maximum_points > 10:
            self.__maximum_points = 10
        self.__resource_points = self.__maximum_points
        self.__hand.append(self.__deck.pop())

    def play_card(self):
        """
        This method simulates when the user plays a card. When they provide the number of the card in their hand, the card 
        is used and resource points are deducted, and the card is moved to the rightmost position in their batallion. The player
        can play a card so long as their resource points doesn't get to or below zero. 
        """
        while self.__resource_points > 0:
            number = int(input("Enter the number of the card from 1 to the length of your current hand: "))
            card = self.__hand[number]
            if card.getResourcePoints() < self.__resource_points:
                self.__resource_points - card.getResourcePoints()
                a_card = self.__hand.pop(number)
                self.__batallion.append(a_card)

        
    def damage(self):
        """
        Method represents the total attacking power in the player's current hand
        """
        for card in self.__batallion:
            total_power += card.getAttackPower()
        return total_power
    
    def opposing_attack(self):
        opp_damage = self.damage()
        for card in self.__batallion:
            card - opp_damage
            if goat_attributes.Card.getHealth() == 0:
                discarded = self.__batallion.pop(self.__batallion[card])
                self.__batallion.pop(self.__batallion[card])
                self.__discarded.append(discarded)
            elif len(self.__batallion) == 0:
                self.getScore() - goat_attributes.Card.getAttackPower()
            elif self.getScore() < 0:
                self.getScore() = 0

    def defeat(self):
        if self.getScore() == 0:
            print(self.__name + " has been defeated")
        elif len(self.__deck) == 0:
            print(self.__name + " has been defeated!")
        else:
            return None
        
    






    




    




    



    