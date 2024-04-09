import sys


# def costum_print(*args, perfix= "coustum Print", **kwargs):
#     output = f"{perfix} {' ' .join(map(str, args))}"
#     print(output, ** kwargs)
#
#
# costum_print("hello", "World", end="\n\n")
#
# costum_print("costum", "print", "test", perfix="[custom")

# def custom_print(*messeges, end="\n", sep=" "):
#     sys.stdout.write(sep.join(messeges)+end)
# custom_print("hello","world", end="!", sep="@",)

#minivally viable product

def outer(x):
    def inner(y):
        return  x * y
    return inner

five_multiplier = outer(5)
three_multiplayer = outer(3)

assert five_multiplier(2) == 10
assert three_multiplayer(4) == 12

# assert 1 > 0 # expression that equals true will do nothing
# assert 1 < 0 # expression that are fals will trigger an assertion error