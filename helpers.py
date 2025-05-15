def rankToNum(rank):
    match rank:
        case "Jack" | "J" | "jack":
            return 11
        case "Queen" | "Q" | "queen":
            return 12
        case "King" | "K" | "king":
            return 13
        case "Ace" | "A" | "ace":
            return 14
        case _:
            return int(rank)

def evenly_split(number, parts):
    base = number // parts
    remainder = number % parts
    result = [base] * parts
    for i in range(remainder):
        result[i] += 1
    return result

def printHelp():
    print("""
sh <player number>: show hand of specified player. Use -s flag to simplify output
cen: show cards in the center
pl <player number> <card> <number/suit?>: play first instance of specified card from specified player's hand. Suit is optional and must be "H", "D", "C", or "S"
pass: current player passes
turn: whose turn is it?
quit: quit the game
help: show these commands""")