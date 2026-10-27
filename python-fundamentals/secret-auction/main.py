





logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

shoraka = {}
print(logo)
name = input("what name ?")
bid = int(input("how much ?"))
shoraka[name]=bid
soal = input("other??")

while soal=="yes":
    print("\n"*100)
    print(logo)
    name = input("what name ?")
    bid = int(input("how much ?"))
    shoraka[name] = bid
    soal = input("other??")

highest = 0
esm = ""
for key in shoraka:
    if shoraka[key] > highest:
        highest = shoraka[key]
        esm = key
print(f"{esm} won")
