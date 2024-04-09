def count_lines(name):
    with open(name, 'r') as file:
        return len(file.readlines())


def count_chars(name):

    with open(name, 'r') as file:
        return len(file.read())


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Number of lines: {lines}")
    print(f"Number of characters: {chars}")


if __name__ == "__main__":
    test("mymod.py")
