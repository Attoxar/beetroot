# # OOP (object oriented programming) conzepts:
# # inheritance
# # incapsulation
# # Polymotphism
# # Abstraction
#
# # Encapsulation - hiding attributes, methodes, other objects in namespaces
# #encapsulation is not a big concept in Python, it works rather like an agreement between gentleman
# # _ = was not meant to use outside of class __= cant use outside of class
# class Klass:
#     _protected_attribute = "some attr"
#     def __private_methode(self):
#         print(self.protected_attribute)
#
#
# demo_object = Klass()
# print(demo_object._protected_attribute)
#
#
# # polymorphism - different objects behaving in the same manner
#
# def poly_function(sequence):
#     for item in sequence:
#         print(item)
# poly_function("12345")
#

# create an object that throws an error everytime you print it
# exit the program everytime you
#instansiation


class MyOwnException(Exception):
    def handle_error(self):
        print("handling error")
class ChildException(MyOwnException):
    error_message = "child error message"
    child_exception = ChildException()
#     child_exception.attribute = "something"
#     child_exception.__dict__
#     print(child_exception.attribute)
class Unprintable:
    def __str__(self):
        return "Hello world"
        #raise MyOwnExeption
    def __add__(self, other):
        return "hello, world"

# # class Klass:
# #     def __str__(self):
# #         pass
# #     def __repr__(self):
# #         pass
#
# demo_object = Unprintable() # instansiation
# print(demo_object + 1)
# print(demo_object)

# create a class whos objects support attributes assignment during instantiation
# create two objects of this class and print their assigned attributes

# class Car:
#     has_wheels = 4
#     has_engine = True
#     color = "Blue"
#
# class Truck(Car):
#     is_large = True
#     Wheels = 6
#
# print("the car is",Car.color".","Truck has",Truck.Wheels, "Wheels")

class Person:
    def __init__(self, name, surname):
         self.name = name
         self.surname = surname

    def greeting(self):
         print(f"hello, {self.name}")

andreas = Person(name="Andreas", surname="Blanck")
andreas.greeting()

class Klass:
    def greeting(self):
        print(f"hello, {self}")

some_object = Klass()
some_object.greeting() # Klass.greeting(some_object)


class Person():
    def __init__(self, name,last_name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, age, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.age = age

student = Student(age="26",name="William", last_name="De Kempel")
print()