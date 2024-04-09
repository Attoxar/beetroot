class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return "Woof Woof"


class Cat(Animal):
    def talk(self):
        return "Meow"


def make_sound(animal):
    return animal.talk()


dog = Dog()
cat = Cat()

print("dogs make: ", make_sound(dog))
print("cats make: ", make_sound(cat))
