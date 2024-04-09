import random


def mathquiz():

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])
    exercise = f"{num1} {operator} {num2}"
    result = eval(exercise)
    return exercise, result


def test():
    exercise, right_result = mathquiz()
    user_answer = input(f"What's the result of {exercise}? ")

    try:
        user_answer = int(user_answer)
        if user_answer == right_result:
            print("Correct!")

        else:

            print("Wrong, the answer is:", right_result)

    except ValueError:

        print("Invalid input. Please enter a number.")


test()
