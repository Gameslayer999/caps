import random
from helpers import evenly_split, rankToNum

class Player:
    def __init__(self, pnum):
        self.playerNum = pnum
        self.hand = []
    
    def showHand(self):
        for card in self.hand:
            print(card)
    
    def showHandSimple(self):
        cards = []
        for card in self.hand:
            cards.append(card.getRank())
        print(", ".join(cards))
    
    def finished(self):
        return len(self.hand) == 0
    
    # returns card if successful, otherwise returns null/none
    def playCard(self, cardRank, *args):
        rank = rankToNum(cardRank)
        multiples = 1
        suit = None
        if len(args) != 0:
            match args[0]:
                case '1' | '2' | '3' | '4':
                    multiples = int(args[0])
                case "H" | "D" | "C" | "S":
                    suit = args[0]
    
        count = 0
        ret = []
        i = 0
        while i < len(self.hand):
            if (suit is None): # didn't specify suit
                if int(self.hand[i].rank) == rank and count < multiples:
                    ret.append(self.hand.pop(i))
                    count += 1
                else:
                    i += 1
            else: # suit specified
                if int(self.hand[i].rank == rank) and self.hand[i].suit == suit:
                    ret.append(self.hand.pop(i))
                i += 1
                
        if len(ret) != multiples:
            # didn't have enough cards to play, so put them back in the hand
            self.hand.extend(ret)
            return []
        else:
            return ret
    
    def finished(self):
        return len(self.hand) == 0
    
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        rank = ""
        suit = ""
        match self.suit:
            case "H":
                suit = "hearts"
            case "D":
                suit = "diamonds"
            case "C":
                suit = "clubs"
            case "S":
                suit = "spades"

        match self.rank:
            case 11:
                rank = "Jack"
            case 12:
                rank = "Queen"
            case 13:
                rank = "King"
            case 14:
                rank = "Ace"
            case _:
                rank = self.rank

        return f"{rank} of {suit}"

    def gte (self, other):
        return self.rank >= other.rank

    def getRank(self):
        rank = ""
        match self.rank:
            case 11:
                rank = "Jack"
            case 12:
                rank = "Queen"
            case 13:
                rank = "King"
            case 14:
                rank = "Ace"
            case _:
                rank = self.rank
        
        return str(rank)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["H", "D", "C", "S"]:
            for rank in range(2, 15):
                self.cards.append(Card(suit, rank))

    def __repr__(self):
        out = ""

        for card in self.cards:
            out += str(card) + "\n"
        
        return out

    def print(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, playerList: list[Player]):
        cardAmounts = evenly_split(len(self.cards), len(playerList))

        count = 0
        for Player in playerList:
            for i in range(cardAmounts[count]):
                Player.hand.append(self.cards.pop())
            count += 1
    
class playStack:
    def __init__(self):
        self.stack = []
    
    # return 1 if success, -1 if not
    def playCard(self, cards):
        #the format of the stack is that it is an array of arrays of different card ranks
        # so, if there were three threes played and then a four, the stack looks like: [[3,3,3]. [4]]
        # this way its easy to check if we have 4 of a kind
        if (len(self.stack) == 0):
            self.stack.append(cards)
            return 1
        else:
            if cards[0].rank == 2: # you can always play a 2
                self.stack.append(cards)
                return 1

            last = len(self.stack) - 1
            if (cards[0].gte(self.stack[last][0])): # if playable
                if (cards[0].rank == self.stack[last][0].rank):
                    self.stack[last].extend(cards)
                else:
                    self.stack.append(cards)
                return 1
            else:
                return -1
    
    #returns 1 if we cleared the stack, -1 if we continue to play
    def clearIfNeeded (self):
        if (len(self.stack) == 0):
            return -1

        last = len(self.stack) - 1
        if (len(self.stack[last]) == 4):
            self.clear()
            return 1
        elif (self.stack[last][0].rank == 2):
            self.clear()
            return 1
        else:
            return -1

    def clear(self):
        self.stack = []

    def showPlayStack(self):
        for cardRank in self.stack:
            for card in cardRank:
                print(card)

