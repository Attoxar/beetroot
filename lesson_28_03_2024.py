# dekorator @ modifys a function and executes the function and returns it


def decorator_creator(title = "MADAM"):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(f'we are using {function.__name__},{title}')
            return function(*args, **kwargs)

        return wrapper
    return decorator
@decorator_creator()
def regular_function():
    print("hello, world")

@decorator_creator()
def fruitfull_function():
    return "hello, world"

#regular_funktion = decorator(regular_funktion)
regular_function()
fruitfull_function()
fruitfull_function()

def funct_with_params(positional, keyword="hello"):
    print(positional)
    print(keyword)

funct_with_params("hello, keyword=world")

class Account:
    account_id = 10
    def print_account_id(self):
        print(self.account_id)

account_belonging_to_John = Account()
account_belonging_to_Beth = Account()

account_belonging_to_Beth.print_account_id()

# print(Account.account_id)
# print(Account.print_account_id())