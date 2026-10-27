import random
import game_data
import art

def choose():
    index = random.randint(0, len(game_data.data)-1)
    choice = game_data.data[index]
    return choice

def check(person1, person2):
    if person1['follower_count'] > person2['follower_count']:
        return 1
    else:
        return 0

def show(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"

def not_same(person1, person2):
    while person1==person2:
        person2 = choose()
    return person2

def game():
    points = 0
    first_person = choose()
    second_person = choose()
    second_person = not_same(first_person, second_person)
    while True:
        print(f"Compare A: {show(first_person)}")
        print(art.vs)
        print(f"Against B: {show(second_person)}")
        user_answer = input("who has more followers ? 'A' or 'B' ? ")
        user_choice = ""
        other_choice = ""
        if user_answer == 'A':
            user_choice = first_person
            other_choice = second_person
        else:
            user_choice = second_person
            other_choice = first_person
        if check(user_choice, other_choice)==1:
            points+=1
            print(f"You're right! Current score: {points}")
        else:
            print(f"You're wrong! Final score: {points}")
            break
        first_person = second_person
        second_person = choose()
        second_person = not_same(first_person, second_person)

print(art.logo)
game()