class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        introduction = (
            f"hello my name is {self.firstname} {self.lastname}. "
            f"I am {self.age} years old."
        )
        print(introduction)



newcomer = Person("Carl", "Johnson", 26)
newcomer.talk()
