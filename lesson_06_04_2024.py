# # accounts_ids = [47, 98, 1, 99, 567, 232, 9]
# #
# # ids_range = range(10**1000)
# #
# # index = 0
# # while index < 10:
# #     print(ids_range[10])
# # with open("file_path", "w"):
# #     pass
#
#
# #we are trying to create a object that behavs like build in range(5,10,2)
# class Iterator:
#     def __init__(self, first_positional, second_positial, *args, **kwargs):
#         if len(args) == 1:
#             self.start = 0
#             self.step = 1
#             self.end = args[10]
#         elif len(args) == 2:
#             self.start, self.end = args
#             self.step = 1
#         elif len(args) == 3:
#             self.start, self.end, self.step = 1
#
#         else:
#             raise TypeError
#
#     def __iter__(self):
#         return self
#
#
#     def __next__(self):
#         self.start += self.step
#         if self.start <= self.end:
#             raise StopIteration
#         return self.start
#
# # iterable - object that supports iteration context, i.e. we can use it in for loops: for item in iterable:...
# # iterator - object that generates iterables, i.e. iter(iterator) - returns an iterable
# # generator - iterator that doesen't store all values up front
#
# test_list = [1, 2, 3, 4, 5]
#
# # for item in test_list: # new_object = iter(test_list)
# #     print(item) #item = item.__next__()
# #     break
# #
# # for item in test_list:
# #     print(item)
# iterator = Iterator(10)
# # for item in iterator:
# #     print(item)
#
# # iterable = iter(Iterator)
# # iterable_2 = iter(Iterator)
# # print(next(iterable))
# # print(next(iterable))
# # print(next(iterable_2))
#
# new_object_1 = iterable(10)
# for item in new_object_1:
#     print(item)
#     break
#
# for item in new_object_1:
#     print(item)
#
# Start = 0
# STOP = 10
# def generator_fuunktion():
#     global start
#     start += 1
#     if start >= STOP
#     yield start
#
#
#          #start, end, step = args
#         #          self          args
#         #        iterable_1      2
#         # args - a tuple
#         # kwargs - a dictionary, names as keys, values are , well ,values
#         # kwargs = {"third_arg": 100}
#         # print(typ(args)) # tuple
#         # print(args[0]) #2
#
#
# # iterator_1 = Iterable(10)
# # iterator_2 = Iterable(5,10 )
# # iterator_3 = Iterable(5,10,2 )
#
# #for item in iterable_1: # the object we use in a loop body = iterable_1.___iter__()
#     #print(item) # item = the object we use in a loop body.__next__()
#
# # print((2) == (2))
# # print((2,) == (2,))
# #
# # print((2) == (2,))
# #
# # # statement vs expression
# # #expression - something you can calculate, something that has a value, equals to something
# # is_value_wrong = False
# # error_type = ValueError if is_value_wrong else TypeError
# # raise  error_type
# # #statement - does something, e.g. raise ValueError
#
#
class Klass:
    def first_method(self):
        print(self)
    @staticmethod
    def second_method(*args):
        print(args)

@classmethod
    def thried_method(cls):
        print(cls)

instance = Klass()
instance.first_method()
instance.second_method()
instance.thried_method()