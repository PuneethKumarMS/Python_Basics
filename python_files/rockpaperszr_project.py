rock = 0
paper = 1
scissors = 2

print(f"{rock},{paper},{scissors}")

user_choice = int(input("Enter your choice: "))
if user_choice > 2 or user_choice < 0:
    print("Invalid choice!.You lose!")
else:
    import random
    computers_choice=random.randint(0,2)
    print(f"Computer choice is: {computers_choice}")

    if user_choice == computers_choice:
        print("It's a tie!")
    elif computers_choice == 0 and user_choice == 2:
        print("You lose!")
    elif user_choice == 0 and computers_choice == 2:
        print("You win!")
    elif computers_choice > user_choice:
        print("You lose!")
    elif user_choice > computers_choice:
        print("You win!")



