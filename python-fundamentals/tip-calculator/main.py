print("welcome to the tip calculator")
total_bill = float(input("what was the total bill ?"))
tip = int(input("how much tip 10 or 12 or 15 ?"))
people = int(input("how many people ?"))
ans = (total_bill + (total_bill * (tip/100)))/people
print(round(ans , 2))