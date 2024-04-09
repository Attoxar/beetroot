# # # # write a decorator that adds a loggin massage befor running a function
# # # import logging
# # from functools import wraps
# # #
# # #
# # # logging.basicConfig(level=logging.INFO)
# # #
# # # def log_before_execution(func):
# # #     @wraps(func)
# # #     def wrapper(*args, **kwargs):
# # #         print(f"loggin warning'{func.__name__}'")
# # #         return func(*args, **kwargs)
# # #     return wrapper
# # #
# # #
# # # @log_before_execution
# # # def test_function():
# # #     print("This is a test function.")
# # #
# # # #
# # # # test_function()
# # # # test_function()
# # # def decorator(function):
# # #     @wraps(function)
# # #         def decorator
# # #             def wrapper(*args, **kwargs):
# # #                 if pre_action:
# # #                 print(f"starting the function {function.__name__}")
# # #                 result = function(*args, **kwargs)
# # #                 if post_action:
# # #                 print(f"completed the function {function.__name__}")
# # #                 return result
# # #     return wrapper
# # # return decorator()
# # #
# # # # a_new_list = [1 + 2]
# # # def decorator_generator(pre_action=True, post_action=True):
# # #     return decorator
# # #
# # # decorator_generator()
# # # @decorator
# # # def some_stuff(): #some_stuff = decorator(some_stuff)
# # #     print("doing some stuff")
# # #
# # # print(some_stuff)
# # #
# # # class Transport:
# # #     pass
# # #
# # # class Car(Transport):
# # #     drives = True
# # #     has_wheels = True
# # # class Boat(Transport):
# # #     has_wheels = False
# # #     floats = True
# # #
# # # class Amphibian(Car, Boat):
# # #     pass
# # # sherp = Amphibian()
# # # print(sherp.has_wheels)
# #
# #
# # # class Car:
# # #     has_wheels = True
# # #     has_engine = True
# # #
# # #     # def runs(self, second_message):
# # #     #     print("i'm driving")
# # #     #     print(f"my color is {self.color}")
# # #     #     print(second_message)
# # #     #     print(self)
# # #
# # # class Truck(Car):
# # #     is_large = True
# # #
# # # my_vw_beetle = Car()
# # # johns_bmw = Car() # instantianating = creating an instance
# # # grandpas_truck = Truck()
# # # #
# # # # print(my_vw_beetle.has_wheels)
# # # # print(grandpas_truck.has_engine)
# # # # print(grandpas_truck.is_large)
# # # #
# # # # johns_bmw.has_no_turn_signals = True
# # # #
# # # # print(johns_bmw.__dict__)
# # # # print(johns_bmw.has_wheels)
# # # # print(grandpas_truck.is_large)
# # #
# # # my_vw_beetle.color = "green"
# # # johns_bmw.color = "black"
# # #
# # # my_vw_beetle.runs("completed driving")
# # # johns_bmw.runs(("driving completed"))
# #
# # class Person:
# #     def __init__(self, name, surname):
# #         self.name = name
# #         self.surname = surname
# #
# #     def greeting(self):
# #         print(f"hello, {self.name}")
# #
# # #magic methodes or dunder methods
# # # dunder is shorted for duble underscore
# #
# # # print(1 + 2) #1. __add__ if wassent found = 2. __radd__
# # # print(1=2) #__eq__
# # # print(str(1)) #1. __str__
# #
# # roman = Person(name= "Roman", surname= "nakutnyi") # instantianating (creating an instance
# # # roman.name = "Roman"
# # # roman.surname = "Nakutnyi"
# # # roman.greeting()
# #
# # andreas = Person()
# # andreas.name = "Andreas"
# # andreas.surname = "Blanck"
# # andreas.greeting()
#
# class Person:
#     name = "some name"
#     accomplishments = ["graduation"]
# person_1 = Person()
# person_1.accomplishments.append("nice job")
# print(person_1.accomplishments)
#
#
# # person_1.name = "william"
# # print(person_1.__dict__)
# # print(Person.name)

