logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
    return n1 + n2
def subtract(n1 , n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def division(n1 , n2):
    return n1 / n2
def solution(operation , n1 , n2):
    if operation=="+":
        return add(n1 , n2)
    elif operation=="-":
        return subtract(n1 , n2)
    elif operation=="*":
        return multiply(n1 , n2)
    elif operation=="/":
        return division(n1 , n2)
    else:
        return 0
way = "n"
answer = ""
while True:
    print(logo)
    if way=="y":
        first_number = answer
    else:
        first_number = float(input("what is the first number ?"))
    print("+\n-\n*\n/")
    operation = (input("pick an operation : "))
    second_number = float(input("what is the next number ?"))
    answer = solution(operation = operation , n1 = first_number , n2 = second_number)
    print(first_number, " ", operation, " ", second_number, " = ", answer)
    print("type 'y' to continue calculating with ", answer, " or type 'n' to start a new calculaton : ")
    way = input()


