# def void_function_squares(number):
#     print(number ** 2)

# void_function_squares(5)

# counter = 5
# while counter > 0:
#     print("sucess!")
#     counter -= 1

# my_list = [1, 2, 3, 4, 5,]
#  dmonstrating_dictionary = {"one": 1, "two": 2, "three": ,3}
# for i in my_list:
#     print(f"i is {i}, success")

# ask a user to input a number, than run a while loopt

#user_count = int(input("put a number  here: "))
#count = (user_count)
#while count in user_count:
#    count += 1
#    print(f"{count}, trys")

#my_list = input("input list here: ")
#for i in my_list:
#        print(i)

#counter = int(input("tell us how often you wanna run the program"))
#while counter >= 1:

#print(f"posetive integer: , {counter}")
#current_output = 0

#for _ in range(counter):
#    print(int(current_output))
#    current_output = not current_output
#    if True:
#        print(1)
#    else:
#        print(0)

#test_list = list(range(10))
#test_list.append(10)
#print(test_list)
#print(test_list[4])
#test_list.pop()
#print(test_list.pop())

#test_list = ["grapefruit", "orange", "bannan"]

#def coustome_in_check(test_list, element):
#    for item in some_list:
#        if "grapefruit" == item:
#           return True
#    return False

#if "grapefruit" in test_list:
#    print(" is in the list")
#else:
#    print(" is not in the list")

#test_string = "python"
#if "yh" in test_string:
#    print("yes")
#
#custome_setting = {
#    "account_shutdown_period": 30,
#    "founds": "3000",
#    "email": "account@gmail.com",
#    "username": "George",
#    "Password": "wqeqwrqwrq766q8rr78q6w7e68q7e",
#}
#if "email" in custome_setting:
#    print("user has confirmed settings")
#else:
#    print("ask user for email over phone")

#test_list.reverse()
#print(test_list)
#test_list.sort()

#test_list.remove(5)
#print(test_list)
#print(max(test_list))

# let's create a list consisting of squares of integers from 0 to 9
#and just print it

#new_list =list(range(10))
#for item in new_list:
#item ** item
#print(item)

# the following 3 lines of code....
#squares = []
#for number in range(10):
#    squares.append(number**2)
#are equivalent to this single line of code, its called a list comprehension
# new_list = [expression_for_each_element_for_variable_in_iterable]
#squares = [number**2 for number in range(10)]
#squares      [numbers**2_____________for number in range(10)]

#zeroes = [0 for _ in range(100)]

import random
numbers = random.randint(1, 10)
#new_list =[]

#print[numbers** in random.randint range(10)]
print([random.randint(0,10) for _ in range(10)])

string_for_slices = "hello world"
print(string_for_slices[len(string_for_slices)::-1])
