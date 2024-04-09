def squared_divide():
    try:
        a = float(input(" enter a number for here wich should be squared:"))
        b = float(input(" enter a second number to divide here:"))
        result = (a ** 2) / b
        return result

    except ValueError:
        print("error: only enter numbers")
        return

    except ZeroDivisionError:
        print("error: unable to divide by zero")
        return


print(squared_divide())
