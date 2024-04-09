def make_operation(operator, *numbers):
    result = None
    if operator == '+':
        result = sum(numbers)
    elif operator == '-':
        result = numbers[0] - sum(numbers[1:])
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num
    return result


print(make_operation('+', 7, 7, 2))  # should be 16
print(make_operation('-', 5, 5, -10, -20))  # should be 30
print(make_operation('*', 7, 6))  # should be 42
