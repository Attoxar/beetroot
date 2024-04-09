import random


my_list = [random.randint(1, 10) for _ in range(10)]
print("my_list: ", my_list)

largest_number = my_list[0]
index = 1

while index < len(my_list):
    if my_list[index] > largest_number:
        largest_number = my_list[index]
    index += 1
    print(f"The largest number is : ", largest_number)
