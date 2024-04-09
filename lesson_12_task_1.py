def print_function_and_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"*** Function '{func.__name__}' ***")
        print(f"Arguments:")
        print("Positional:", *args)
        print("Keyword:", *[f"{key}={value}" for key, value in kwargs.items()])
        print("*** End of {Function.__name__} ***")
        return func(*args, **kwargs)
    return wrapper


@print_function_and_arguments
def add(x, y):
    return x + y


@print_function_and_arguments
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(2, 3, 4)
add(4, 7)