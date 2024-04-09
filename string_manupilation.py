def first_and_last_two_chars(string):

    if len(string) < 2:
        return "empty string"
    else:
        return string[:2] + string[-2:]


input_strings = ["helloworld", "my", "x"]
for input_string in input_strings:
    result = first_and_last_two_chars(input_string)
    print(f"sample string: '{input_string}'")
    print(f"Expected Result: '{result}'")
    print()
