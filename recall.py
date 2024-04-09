# import sys
# from pprint import pprint
#
# pprint(sys.path)
#
# sys.path.insert(0, __object=),'file location')
# import os.path
# import random
#
# import package_exemple
#
# pprint(sys.path)
# print(random.randint(1,10))
# print(random.shuffle(1,2,3,4,5))
# print(random.choice(1,2,3,4,5))
#
# print(os.path.exists("filepath"))
# print(os.path.exists(filepath))

# import hello_world
# print(hello_world.hello_variable)
#print(hello_world.mutable_global_variable)

new_list = []
for item in range(10):
    new_list.append(item)

new_list = [item**2 for item in range(10)]

new_dictionary = {}
for item in range(10):
    new_dictionary[item] = item**2

new_dictionary = {item: item for item**2 in range(10)}


