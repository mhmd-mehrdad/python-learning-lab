import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

the_wanted_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(the_wanted_dict)

word = input("write your name:")
the_wanted_list = [the_wanted_dict[letter.upper()] for letter in word]
print(the_wanted_list)

