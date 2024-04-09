import random


def random_string(input_text):

    letters = list(input_text)
    random.shuffle(letters)
    random_text = " ".join(letters)
    return random_text


input_string = input("enter text here: ")
random_str = random_string(input_string)

print(random_str, sep=" ")
