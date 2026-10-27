import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def total_score(cards):
    total = 0
    for card in cards:
        total += card
    return total
careee = [1 , 2  , 3]
if total_score(careee) < 100:
    print("yes")


def show_cards(cards):
    for card in cards:
        print(card)


player_cards = []
computer_cards = []

def game_rules(player_cards, computer_cards, permit):
    
    while permit=="y":
        player_cards.append(random.randint(1, 11))
        print(f"your cards: {player_cards}, current score: {total_score(player_cards)}\n"
              f"computer cards: {computer_cards}")
        permit = input("another ? ")
        if permit== "n":
            while total_score(computer_cards) < 17:
                computer_cards.append(random.randint(1, 11))
            print(f"player cards = {player_cards} player score: {total_score(player_cards)}\ncomputer's cards = {computer_cards} computer score: {total_score(computer_cards)}")
            if total_score(player_cards)<=21 and total_score(computer_cards)<=21:
                if total_score(computer_cards) >= total_score(player_cards):
                    print("you lose")
                else:
                    print("you win")
            if total_score(player_cards)>21 and total_score(computer_cards)<=21:
                print("you lose")
            if total_score(player_cards)<=21 and total_score(computer_cards)>21:
                print("you win")
            if total_score(player_cards)>21 and total_score(computer_cards)>21:
                if total_score(player_cards)>=total_score(computer_cards):
                    print("you lose")
                else:
                    print("you win")

permission = input("do you wanna play ? y or n : ")
while permission=="y":
    player_cards.clear()
    computer_cards.clear()
    print(logo)
    player_cards.append(random.randint(1 , 11))
    player_cards.append(random.randint(1 , 11))
    computer_cards.append(random.randint(1 , 11))
    print(f"your cards: {player_cards}, current score: {total_score(player_cards)}\n"
          f"computer's first card: {computer_cards}")
    second_permission = input("type 'y' to get another card, type 'n' to pass: ")
    game_rules(player_cards, computer_cards, second_permission)
    permission = input("do you wanna play ? y or n : ")

