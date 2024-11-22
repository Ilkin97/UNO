import random
from build_deck import build_deck

def shuffle_deck(deck):
    for card_pos in range(len(deck)):
        rand_pos = random.randint(0, 107)
        deck[card_pos], deck[rand_pos] = deck[rand_pos], deck[card_pos]

    return deck

def draw_cards(num_cards):
    cards_draw = [ ]
    for x in range(num_cards):
        cards_draw.append(uno_deck.pop(0))
    
    return cards_draw

def show_hand(player, player_hand):
    print("Player {}'s Turn".format(player + 1))
    print("Your Hand")
    print("------------------")
    y = 1
    
    for card in player_hand:
        print("{} {}".format(y, card))
        y += 1
    print("")
    
def can_play(colour, value, player_hand):
    for card in player_hand:
        
        if "Wild" in card[0]:
            return True
        elif colour in card or value in card:
            return True
    
    return False

uno_deck = build_deck()
uno_deck = shuffle_deck(uno_deck)
discards = [ ]
print(uno_deck)


players = [ ]
colours = ["Red", "Green", "Yellow", "Blue"]
num_players = int(input("How many players? >> "))

while num_players < 2 or num_players > 4:
    num_players = int(input("Invalid. Please enter a number between 2-4. How many players? >> "))

for player in range(num_players):
    players.append(draw_cards(5))

player_turn = 0
play_direction = 1
playing = True
discards.append(uno_deck.pop(0))
split_card = discards[0].split(" ", 1)
current_color = split_card[0]

if current_color != "Wild":
    card_val = split_card[1]
else:
    card_val = "Any"

while playing:
    show_hand(player_turn, players[player_turn])
    print("Card on top of discard pile: {}".format(discards[-1]))
    
    if can_play(current_color, card_val, players[player_turn]):
        card_chosen = int(input("Which card do you want to play? >> "))
        
        while not can_play(current_color, card_val, [players[player_turn][card_chosen - 1]]):
            card_chosen = int(input("Not a valid card. Which card do you want to play? >> "))
        print("You played {}".format(players[player_turn][card_chosen - 1]))
        discards.append(players[player_turn].pop(card_chosen - 1))

    else:
        print("You can't play. You have to draw a card.")
        players[player_turn].extend(draw_cards(1))
    print("")
    player_turn += play_direction
    
    split_card = discards[0].split(" ", 1)
    current_color = split_card[0]
    
    if len(split_card) == 1:
        card_val = "Any"
    else:
        card_val = split_card[1]
        
    if current_color == "Wild":
        for x in range(len(colours)):
            print("{} {}".format(x + 1, colours[x]))
        new_colour = int(input("What colour would you like to choose?  >> "))
        
        while new_colour < 1 or new_colour > 4:
            new_colour = int(input("What colour would you like to choose?  >> "))
        current_color = colours[new_colour-1]
    
    if card_val == "Reverse":
        play_direction = play_direction * -1
    elif card_val == "Skip":
        player_turn += play_direction
    elif card_val == "Draw Two":
        players[player_turn].extend(draw_cards(2))
    elif card_val == "Draw Four":
        player[player_turn].extend(draw_cards(4))
    
    player_turn += play_direction
    if player_turn == num_players:
        player_turn = 0
    elif player_turn < 0:
        player_turn = num_players - 1