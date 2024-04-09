class Dog:
    def __init__(self, age):
        self.age = age

    def human_age(self):
        dog_years = self.age
        human_years = dog_years * 7
        return human_years


human_age_input = int(input("Enter the dog's age in human years: "))
dog1 = Dog(human_age_input)
print("The dog's age in human years is:", dog1.human_age())
