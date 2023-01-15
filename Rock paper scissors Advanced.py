import random


def play():
    user_input = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer_input = random.choice(["r", "p", "s"])
    print(computer_input)
    if user_input == computer_input:
        return "It's a tie"
    if is_win(user_input, computer_input):
        return "You won"
    return "You lost"


def is_win(user_input, computer_input):
    if (user_input == "r" and computer_input == "s") or (user_input == "p" and computer_input == "r") \
            or (user_input == "s" and computer_input == "p"):
        return True


print(play())
