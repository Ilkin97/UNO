def build_deck():
    deck = [ ]
    colours = ["Red", "Green", "Yellow", "Blue"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]
    
    for colour in colours:
        for value in values:
            card_val = "{} {}".format(colour, value)
            deck.append(card_val)
            
            if value != 0:
                deck.append(card_val)
    
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])    
    print(deck)
    
    return deck

uno_deck = build_deck()