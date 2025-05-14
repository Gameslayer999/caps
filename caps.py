from player import playStack, Player, Card, Deck
from helpers import printHelp

def play():
    center = playStack()
    deck = Deck()
    deck.shuffle()
    players = []

    while (True):
        try:
            numPlayers = int(input("How many people are playing?: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    for i in range(numPlayers):
        players.append(Player(i + 1))

    deck.deal(players)

    playerTurn = 1
    printHelp()
    
    # play 3 of spades first
    for player in players:
        card = player.playCard(3, "S")
        if card is not None:
            center.playCard(card)

    print ("It is player 1's turn")
    #game loop
    while (True):
        nextMove = input()
        command = nextMove.split(" ")

        try:
            match (command[0]):
                case "sh":
                    if (len(command) == 2):
                        players[int(command[1]) - 1].showHand()
                    elif len(command) == 3 and command[2] == "-s":
                        #-s flag was used
                        players[int(command[1]) - 1].showHandSimple()
                    else:
                        print("Invalid command")

                case "cen":
                    center.showPlayStack()

                case "pl":
                    card = players[int(command[1]) - 1].playCard(command[2])
                    if card is None:
                        print("That card is not in your hand, try again")
                    elif (center.playCard(card) == -1):
                        #if card cannot be played, return it to the player's hand
                        players[int(command[1]) - 1].hand.append(card)
                        print("Can't play that card right now, try again")
                    else:
                        # check if we need to clear the center
                        if (center.clearIfNeeded() == -1):
                            # didn't need to clear, so we continue playing
                            playerTurn += 1
                            if (playerTurn > len(players)):
                                playerTurn = 1

                            print(f"It is now player {playerTurn}'s turn.")
                        else:
                            print(f"Cleared the center, now player {playerTurn} needs to put down a card to start.")

                case "pass":
                    playerTurn += 1
                    if (playerTurn > len(players)):
                        playerTurn = 1

                    print(f"It is now player {playerTurn}'s turn.")

                case "turn":
                    print(f"It is now player {playerTurn}'s turn.")

                case "quit":
                    break

                case "help":
                    printHelp()
                    
                case _:
                    print("Invalid command.")
        except TypeError:
            print("Invalid command")
        except IndexError:
            print("Player does not exist")


def main():
    play()


if __name__ == "__main__":
    main()