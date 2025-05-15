from player import playStack, Player, Card, Deck
from helpers import printHelp
def startGame(): #starts game by asking how many people are playing
    players = []
    
    while (True):
        try:
            numPlayers = int(input("How many people are playing?: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    for i in range(numPlayers):
        players.append(Player(i + 1))
    
    return players

def playcli(players):
    center = playStack()
    deck = Deck()
    deck.shuffle()
    deck.deal(players)

    # variables to track game state
    playerTurn = 1
    playersPassed = 0
    finishOrder = []
    printHelp()
    
    # play 3 of spades first
    for i in range(len(players)):
        card = players[i].playCard(3, "S")
        if len(card) == 1:
            center.playCard(card)
            playerTurn = i + 2
            
            if (playerTurn > len(players)):
                playerTurn = 1
        

    print (f"It is player {playerTurn}'s turn")
    #game loop
    while (True):
        nextMove = input()
        command = nextMove.split(" ")

        try:
            match (command[0]):
                case "sh":
                    player = players[int(command[1]) - 1]
                    
                    if (len(command) == 2):
                        player.showHand()
                    elif len(command) == 3 and command[2] == "-s":
                        #-s flag was used
                        player.showHandSimple()
                    else:
                        print("Invalid command")

                case "cen":
                    center.showPlayStack()

                case "pl":
                    player = players[int(command[1]) - 1]
                    
                    if int(command[1]) != playerTurn:
                        print("It is not that player's turn right now.")
                        continue
                    
                    cards = []
                    if len(command) == 4:
                        # either asked for multiple cards or a specific card
                        # let the player function sort it out
                        cards.extend(player.playCard(command[2], command [3]))
                    else:
                        cards = (player.playCard(command[2]))
                    
                    if len(cards) == 0:
                        print("That card is not in your hand, try again")
                    elif (center.playCard(cards) == -1):
                        #if card cannot be played, return it to the player's hand
                        player.hand.append(cards)
                        print("Can't play that card right now, try again")
                    else:
                        # check if player is out of cards, and if so, add to the list of finished players
                        if player.finished():
                            finishOrder.append(player.playerNum)
                            print(f"Player {playerTurn} is finished.")
                        
                        # check if we need to clear the center
                        if (center.clearIfNeeded() == -1):
                            # didn't need to clear, so we continue playing
                            playerTurn += 1
                            playersPassed = 0
                            if (playerTurn > len(players)):
                                playerTurn = 1

                            print(f"It is now player {playerTurn}'s turn.")
                        else:
                            print(f"Cleared the center, now player {playerTurn} needs to put down a card to start.")

                case "pass":
                    playerTurn += 1
                    playersPassed += 1
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

        if playersPassed == len(players) - 1:
            center.clear()
            print(f"All players passed, so center is cleared. Player {playerTurn} needs to put down a card to start.")
        
        
        #check if the last person got rid of cards
        while players[playerTurn - 1].finished():
            print(f"player {playerTurn} is finished, moving to next player...")
            playerTurn += 1
            print(f"It is now player {playerTurn}'s turn.")


def main():
    playcli(startGame())


if __name__ == "__main__":
    main()