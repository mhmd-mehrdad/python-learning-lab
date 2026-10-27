import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("guess a letter...").lower()

number = 0
for x in chosen_word:
    number+=1
placeholder = "_" * number

display = []
for x in chosen_word:
    if guess==x:
        display.append(guess)
    else:
        display.append("_")

print(display)
if all(item == '_' for item in display):
    print(stages[lives])
    lives-=1


def show_display():
    for x in display:
        print(x,end="")
    print("")

show_display()

while "_" in display:
    guess = input("guess a letter...").lower()
    n = 0
    a = 1
    b = 0
    for x in chosen_word:
        if guess == x:
            display[n] = guess
            n+=1
            b+=1
        else:
            n+=1
    if a > b:
        print(stages[lives])
        lives-=1
    show_display()




