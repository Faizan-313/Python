import random

choices = ["Rock", "Paper", "Scissors"]
char = 'y'
while char =='y':
    try:
        u_c = int(input("What do you choose? Type 0 for Rock , 1 for paper or 2 for the scissors.\n"))
        if u_c > 2 or u_c < 0:
            print("Invalid input")
            continue
        print(f"you choose {choices[u_c]}")
        c = random.randint(0,2)
        print(f"Computer chose {choices[c]}")
        if u_c == 0 and c == 2 or u_c == 1 and c == 0 or u_c == 2 and c == 1:
            print("you win")
        elif u_c == c:
            print("Draw")
        else:
            print("You Lose")
    except ValueError:
        print("Invalid input")
        continue
    char = input("for playing agin press y for exit e \n").lower()


