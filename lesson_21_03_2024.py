# dict comprehension
#
# new_list = []
# for item in range(10):
#     new_list.append(item**2)
#
#
# new_list = [item**2 for item in range(10)]
#
# new_dictionary = {}
# for element in range(10):
#     new_dictionary[element] = element**2
#
# new_dictionary = {element:element**2 for element in range(10)}

#
# keys_values_list = [0,0], [1,1], [2,4], [3,9], [4,16]
# [0,0]
# key, value = [0, 0]
# #print(key)
# #print(value)
#
# new_keys_values_list = {key: value**2 for key, value in keys_values_list}
# new_dictionary = {}
# for key, value in keys_values_list:
#     new_dictionary[key] = value
#
#
# print(new_keys_values_list)
#
# # a = 10
# # b = 11


# items_list = ["water", "milk", "bread"]
# #
# new_dict ={}
# for item in items_list:
#     new_dict[item] = item.upper()
# print(new_dict)
# new_dict = {item: item for item in items_list}
# print(new_dict)
#
# item_upper = [item.upper() for item in items_list]
# my_dictionary = dict(zip(items_list, item_upper))
# # print(my_dictionary)
#
#
# new_dict = {item: item_upper for item in items_list}
# print(my_dictionary)

try:
    file = open("temp", "w")
    raise Exception
    file.write("Hello world")
except:
    pass
file.close()