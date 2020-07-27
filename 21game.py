from random import randint
from lunalib import getint

win = 21
current = 0
winner = "CPU"


def player_turn(current, win):
    player_choice = getint(
        "Player's turn!\nChoose a number between 1 and 3, inclusive!\n", 1, 3
    )
    if (current + player_choice) > win:
        current += player_choice
    elif (current + player_choice) == win:
        current += player_choice
    else:
        print(f"The count goes from {current} to {current + player_choice}")
        current += player_choice
    return current


print("Take turns choosing a number from 1-3. The player who lands on 21 wins.")

gofirst = getint(
    "If you want to go first press 1.\nIf you want to go second, press 2.\n", 1, 2
)

if gofirst == 1:
    player_choice = 0
    while player_choice < 1 or player_choice > 3:
        player_choice = getint(
            "Choose a number between 1 and 3, inclusive, to start off.\n", 1, 3
        )
    current += player_choice

while current < win:
    if current < 18:
        cpu_choice = randint(1, 3)
    else:
        cpu_choice = win - current
    print(
        f"The computer chose {cpu_choice}!\nThe count goes up from {current} to {current + cpu_choice}!"
    )
    current += cpu_choice
    if current == win:
        print("Copmuter wins!")
        break
    current = player_turn(current, win)

    if current == win:
        print(f"Current: {current}, Win: {win}\nYou Win!")
    elif current > win:
        print(
            f"Uh, whoops. The goal is to reach {win}, you accidentally went over it by {win - current}."
        )
        print("You lose. :(")
