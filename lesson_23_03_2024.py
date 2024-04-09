# scopes
# 1. build in - print
# 2. global -func_name
# 3. local - some_ver in regards to func_name
# 4. non local - some_ver in regards to func_name_2


# global_exempel = 100500
#
# def func_name():
#     global_exempel.append("test")
#     local_variable = 3
#     def inner(:)
#         local_variable = 4
#
# func_name()
# print(global_exempel)



# def func_name():
#     some_ver = 3
#     print(some_ver)
#
#     global_exempel = 2
#     def func_name_2():
#         another_ver = 4
#
#
# func_name()
# print(global_exempel)


#name space

# def demonstration():
#     some_variable = "test"
# class Klass:
#     some_variable = "test"
#     print(Klass.some_variable)

# enclosed_list = [[1,2,3], [4,5], [6], [7,8,9,10]]
# new_list = [number for element in enclosed_list for number in element]
# # for element in enclosed_list:
# #     #new_list += enclosed_list
# #      for number in element:
# #          new_list.append(number)
# print(new_list)
#
# # check = True
# # while True:
# #     user_input = input("please type a number from 0 to 9: ")
# #     if user_input.isdigit() and int(user_input) in range(10):
# #         print("right")
# #         break
# #     user_input = input("try again")
#
# def multiplicator_factory(multiplicator):
#     def inner(number):
#         return multiplicator * number # multiplicator is still stored in memory after "multiplicator_factory" end of execution, its still called "closure"
#     return inner
#
# three_multiplicator = multiplicator_factory(3)
# six_multiplicator = multiplicator_factory(6)
#
# print(three_multiplicator(3)) #6
# print(six_multiplicator(9)) # 54
#
# def demo(some_param):
#     demo_variable = 4
#     print(some_param)
#     print(demo_variable)
#     print("i am on line 27")
#
# demo("hello")
# demo("another Hello")
#

# create a function that takes 1 paramenter, it will be anonother function later
#inside outer print the parameter and than return the parameter
#create another function in the global scope name it inner
#the body of the inner function does whatever you like
# run the outer function provide the inner  as a parameter and assaign the result back to the the inner name in the global scope

# def outer():
#     print("test")
#     return outer()
#     def inner():
#         a = 1
#         b = 2
#     print(outer89 + inner())
#
# outer()

def commander(dekorated_function):
    def wrapper(*args, **kwargs):
        print("starting my assignment")
        result = dekorated_function()
        print("done")
        return result
    return wrapper

@commander
def inner():
    print("doing inner job")

@commander
def new_inner(first_name, second_name):
    print(first_name)
    print(second_name)
    return f"{first_name} {second_name}"
#
#
# # inner = commander(inner)
#
# inner()
# inner()
# inner()

# def test():
#         user_input = input("put a number here :")
#         user_input2 = input("put another number here: ")
#         result = int(user_input.isdigit()) * int(user_input2.isdigit())
#         print(result)
#
# test()
