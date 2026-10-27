print(r"""
*******************************************************************************

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
*******************************************************************************
""")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = input("you go left or right ?")
if a == "left":
    b = input("swim or boat ?")
    if b == "boat":
        c = input("ok you're in...which door(red, blue, yellow) ?")
        if c == "yellow":
            print("$1000000")
        elif c == "red":
            print("fireeeee...game over")
        elif c == "blue":
            print("beast...game over")
        else:
            print("GAME OVER")
    else:
        print("crocodile...game over")
else :
    print("hole...game over")
