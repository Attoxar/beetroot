# data types:
# int: whole numbers
# float:
# bool:
# string:
# sets:
#tuple:
# dict:
# list:
# none: no build in function for that

#build in  functions:
# print()
# input()
# range()
# min()
# sum()
# len()
# type()

#lists
# test_list = list(range(11))
# #print(type(test_list))
#
# some_list = ["hello world"]
# some_dict = list({"one": 1, "two": 2})
# print("one" in some_dict)
# assert some_list[0] == "hello world"
# #some_list = []
# #for element in "hello world":
# # some_list.append(element)
#
# empty_tuble = ()
# empty_dict = {}
# empty_set = set()

# for element in ["one", "", [], 2, 3, 4, 5]:
#     print(element)

# a = "hello"
# b = "world"
# a, b = b, a
# print(b)

# demo_list = list(range(10))
# print(demo_list.append(10)) demo_list.extend([11,12,13]) adds 3 items
# print(len(demo_list))
# print(demo_list.remove(10)) #removes by value
# #demo_list.pop() removes the last one or with a value it removes coresponding to the index( removes by position)
# print(50 in demo_list) #False
# print(5 in demo_list) # True
# print(demo_list[1])
# print(demo_list[2:6])

# demo_dictionary = {1: "one", 2: "two", 3: "three"}
# #demo_dictionary.get(1)
# # for key, value in demo_dictionary.items():
# #     if key == 2
# #         print(value)
# #print(demo_dictionary.)
# demo_dictionary[4] = "four"
# print(demo_dictionary)

# list_of_unsorted_lists = [[2,45,1], [4,342,1], [1,2,5,-100]]
# for inner_list in list_of_unsorted_lists:
#     inner_list.sort()
# #print(list_of_unsorted_lists)
# print([sorted(inner_list) for inner_list in list_of_unsorted_lists])

def function():
    def inner():
        print("hello, world")
    return inner
function()()
#inner = function()
#inner() calling an inner function with ()()
#scopes=
# globale,
# local,
# buildins,
# nonlocal

