import re


class User:
    def __init__(self):
        email = input("Enter your email address: ")
        self.email = email
        self.validate(email)

    @classmethod
    def validate(cls, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")


try:
    user = User()
    print("Valid email:", user.email)
except ValueError as e:
    print(e)
