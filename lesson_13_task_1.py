def count_local_variables(func):
    code = func.__code__
    local_variables = code.co_varnames
    return len(local_variables)


def example_function():
    var1 = 5
    var2 = "test"
    var3 = True


num_local_variables = count_local_variables(example_function)
print("Number of local variables:", num_local_variables)
