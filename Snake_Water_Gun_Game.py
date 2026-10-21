print("-------Welcome to Snake, Water, Gun Game-------\n")
import random

rounds = 0
userpoint = 0
computerpoint = 0

while rounds < 10:
    choices = ["Snake", "Gun", "Water"]
    choice = random.choice(choices)
    user_input = input("Enter Snake for s: Water for w: Gun for g: ")

    if user_input == "s" and choice == "Water":
        userpoint += 1
        rounds += 1
    elif user_input == "s" and choice == "Gun":
        computerpoint += 1
        rounds += 1
    elif user_input == "s" and choice == "Snake":
        rounds += 1
    elif user_input == "w" and choice == "Water":
        rounds += 1
    elif user_input == "w" and choice == "Gun":
        userpoint += 1
        rounds += 1
    elif user_input == "w" and choice == "Snake":
        computerpoint += 1
        rounds += 1
    elif user_input == "g" and choice == "Gun":
        rounds += 1
    elif user_input == "g" and choice == "Snake":
        userpoint += 1
        rounds += 1
    elif user_input == "g" and choice == "Water":
        computerpoint += 1
        rounds += 1

    print(f"Computer: {choice} | You:{userpoint} Comp:{computerpoint}")

if userpoint > computerpoint:
    print("Congratulation ! You win.")
    print(f"Your points is {userpoint}")
elif userpoint < computerpoint:
    print("Sorry ! You lose... Try Again!")
else:
    print("Draw")
