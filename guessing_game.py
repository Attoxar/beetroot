import random


def game():

    random_number = random.randint(1, 10)
    guess = input("guess a number from 1 to 10: ")
    if guess == random_number:
        print("you win")
    else:
        print("You lose, the number was: ", random_number)


game()
