import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo, "\nwelcome to the number guessing game!\ni'm thinking of a number between 1 to 100.")
the_number = random.randint(1, 100)
level = input("choose a difficulty level. type 'easy' or 'hard': ")
count = None
if level=="easy":
    count = 10
elif level=="hard":
    count = 10
else:
    print("Invalid choice")
game_over = False
while count > 0 and game_over==False:
    print(f"you have {count} attempts remaining to guess the number.")
    player_guess = int(input("make a guess: "))
    if player_guess == the_number:
        print("YOU WON!!!")
        game_over = True
    elif player_guess > the_number:
        print("Too high\nguess again.")
        count-=1
    elif player_guess < the_number:
        print("Too low\nguess again.")
        count-=1
if count==0:
    print("you run out")
