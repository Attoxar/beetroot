import random


my_list1 = []
while len(my_list1) < 10:
    my_list1.append(random.randint(1, 10))
print("my first list :", my_list1)

my_list2 = []
while len(my_list2) < 10:
    my_list2.append(random.randint(1, 10))
print("my second list: ", my_list2)

my_list_no_dublicates = []
index = 0
while index < len(my_list1):
    if my_list1[index] in my_list2 and my_list1[index] not in my_list_no_dublicates:
        my_list_no_dublicates.append(my_list1[index])
    index += 1

print("integers with no dublicates in both lists: ", my_list_no_dublicates)
