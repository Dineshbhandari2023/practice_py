print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")

choice1 = input("you'r at a crossroad, where do you want to go? Type'left' or 'Right'.").lower()

if choice1 == "left":
    # continues to the game.
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for the boat. Type 'Swim' to swim across.").lower()
    if choice2 == "wait":
        # continues the game.
        choice3 = input("So, now here is the three colour door Red, Blue and yellow. Which colour would you choose? Type 'Red','Blue' or 'Yellow'.").lower()
        if choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over!!!. You loose.")
    else:
        print("You just fell into the hole. Game Over!!!")
else:
    print("you fell into the hole. Game Over!!!.")


