import random
while True:
    user_action = input("enter a choice (rock.paper,scissors)")
    possible_action=["rock, paper,scissors"]
    computer_action= random.choice(possible_action)
    print(f"You chose {user_action},computer chose{computer_action}")
    if user_action== computer_action:
        print("it is a tie")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("you win")
        else:
         print("you lose")
    elif user_action=="paper":
        if computer_action=="rock":
            print("you win")
        else:
         print("you lose")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("you win")
        else:
         print("you lose")
    play= input("play again ?")
    if play != "y":
        break