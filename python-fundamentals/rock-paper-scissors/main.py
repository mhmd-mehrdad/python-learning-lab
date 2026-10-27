import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock , paper , scissors]

player_choice = choices[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))]

index = random.randint(0 , 2)
computer_choice = choices[index]

if player_choice == computer_choice :
    print("your choice = ", player_choice, "\ncomputer's choice = ", computer_choice
          , "\nDRAW")
elif player_choice == rock and computer_choice == paper :
    print("your choice = ", player_choice, "\ncomputer's choice = ", computer_choice
          , "\nLoss")
elif player_choice == rock and computer_choice == scissors :
    print("your choice = ", player_choice, "\ncomputer's choice = ", computer_choice
          , "\nWIN")
elif player_choice == paper and computer_choice == rock :
    print("your choice = ", player_choice, "\ncomputer's choice = ", computer_choice
          , "\nWIN")
elif player_choice == paper and computer_choice == scissors :
    print("your choice = ", player_choice, "\ncomputer's choice = ", computer_choice
          , "\nLOSS")
elif player_choice == scissors and computer_choice == rock :
    print("your choice = ", player_choice, "\ncomputer's choice = ", computer_choice
          , "\nLOSS")
elif player_choice == scissors and computer_choice == paper :
    print("your choice = ", player_choice, "\ncomputer's choice = ", computer_choice
          , "\nWIN")
else :
    print("NOT VALID")