from enum import Enum

class ranks(Enum):
    "J" = 11
    "Q" = 12
    "K" = 13
    "A" = 14

class Player:
    def __init__(self, pnum):
        self.playerNum = pnum
        self.cards = []
    
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def gte (self, other):
        return self.rank >= other.rank
    
class playStack:
    def __init__(self):
        self.stack = []
    