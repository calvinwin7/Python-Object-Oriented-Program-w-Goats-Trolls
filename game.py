import player
import goat_attributes

def print_players(player, opponent):
    """
    This function returns a detailed string representation of the current statistics of the player and opponent, including aspects
    such as their name, score, resoruce points, batallion, deck, current hand. 
    """
    print(repr(opponent))
    print()
    print(repr(player))

def take_turn(player, opponent):
    """
    This function prompts a player turn, and prints a detailed string representation of the player's and opponents batallion
    if a card is played properly. A list of commands is offered to the user in order for them to execute properties such as ending
    a player's turn, showing detailed information about a card in a batallion, etc. 

    """
    player.start_turn()
    print_players(player, opponent)

    while True:
        command = input(str(player) + " >>")
        tokens = command.split()
        if tokens[0].upper() == "Q":
            break
        elif tokens[0].upper() == "P":
            number = int(tokens[1])
            if player.play_card(number):
                print_players(player, opponent)
            else:
                print("Invalid card")
        elif tokens[0].upper == "H":
            print(player.__repr__(player.getCard()))
        elif tokens[0].upper == "B":
            print(player.__repr__(player.getBatallion()))
        elif tokens[0].upper == "E":
            print(player.__repr__.getBatallion())
        elif tokens[0].upper == "I":
            commands = ["H, B, E, P, Q, I"]
            print("Here are the list of commands:" + commands)
        else:
            print("Invalid command")
            continue


def take_damage(opponent):
    return opponent.opposing_attack()
    

def main():
    p1_name = input("Enter your name P1")  
    p1 = player.Player(p1_name, player.Player.getBatallion())

    p2_name = input("Enter your name P2")
    p2 = player.Player(p2_name, player.Player.getBatallion())

    while p1.getScore() > 0 or p2.getScore() > 0:
        take_turn(p1, p2)
        take_damage(p2)
        p1, p2 = p2, p1

        
    if p1.getScore() <= 0:
        print(p1 + " has been defeated! " + p2 + " has won!")
    elif p2.getScore() <= 0:
        print(p2 + " has been defeated! " + p1 + " has won!")


if __name__ == "__main__":
    main()

        
                  







