MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 250,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def give_report():
    for item in resources:
        print(f"{item} = {resources[item]}\nmoney = {money}")

def start_point():
    a = input("what do you want ? ")
    if a=='report':
        give_report()
        return 1
    elif a=='nothing':
        print('ok bye')
        return 1
    else:
        return a

def check_resources(drink):
    for item in MENU:
        if drink==item:
            for ingredient in MENU[item]['ingredients']:
                if MENU[item]['ingredients'][ingredient] > resources[ingredient]:
                    print(f"not enough {ingredient}")
                    return 0
            return drink
    return 0

def cash_receiver(drink):
    value = 0
    for item in MENU:
        if drink==item:
            value = MENU[item]['cost']
    quarters = int(input("how many quarters ?"))
    dimes = int(input("how many dimes ?"))
    nickel = int(input("how many nickels ?"))
    pennies = int(input("how many pennies ?"))
    total = quarters*0.25 + dimes*0.1 + nickel*0.05 + pennies*0.01
    global money
    money+=total
    if total < value:
        print("not enough money!!!")
        return 0
    else:
        change = total - value
        print(f"You're change is {round(change, 2)}")
        return drink

def coffee_maker(drink):
    for item in MENU:
        if item==drink:
            index=0
            for ingredient in MENU[item]["ingredients"]:
                resources[ingredient]-=MENU[item]["ingredients"][ingredient]
            print("DRINK IS READY!!!☕")




def main_machine():
    while True:
        ans = start_point()
        check = check_resources(ans)
        if check != 0:
            a = cash_receiver(check)
            if a != 0:
                coffee_maker(a)






main_machine()
