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
            batallion += str(self.__batallion(i))
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

        
    




    



    