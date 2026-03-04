import random

choices = ("k", "p", "n")
emoji = {
    "k": "🪨",
    "p": "📃",
    "n": "✂️"
}

def user():
    while  True:
        user_choice = input("Kamen, papier noznice? (k,p,n) ").lower()
        if user_choice in choices:
            print(f"vybral si si {emoji[user_choice]}")
            return user_choice
        else:
            print("vyber len z uvedenych moznosti")

def computer():
    computer_choice = random.choice(choices)
    print(f"pocitac si vybral {emoji[computer_choice]}")
    return computer_choice

def find_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("remiza")
    elif (
        (user_choice == "k" and computer_choice == "n") or
        (user_choice == "n" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "k")):
        print("vyhral si. ")
    else:
        print("prehral si. ")

def play_game():
    while True:
        user_choice = user()
        computer_choice = computer()
        find_winner(user_choice, computer_choice)

        shoul_continue = input("chces pokracovat? (y/n): ")
        if shoul_continue == "n":
            print("tak niekedy nabuduce. Ahoj. ")
            break

play_game()
