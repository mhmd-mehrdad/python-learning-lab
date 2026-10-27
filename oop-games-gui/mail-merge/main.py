from pathlib import Path

Path("Output/ReadyToSend").mkdir(parents=True, exist_ok=True)


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

    
        

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
print(letter)

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
print(names)

for name in names:
    clean_name = name.strip()
    new_letter = letter.replace("[name]", clean_name)

    with open(f"Output/ReadyToSend/letter_for_{clean_name}",mode="w") as sent_letters_file:
        sent_letters_file.write(new_letter)
        print(new_letter)

# new_letter = letter.replace("[name]", names)
# print(new_letter)
