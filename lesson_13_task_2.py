def outer():
    def inner():
        return "here is the inner function"

    return inner


func = outer()

result = func()
print(result)
