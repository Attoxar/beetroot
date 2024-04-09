num = 1
result_list = []
while num <= 100:
    if num % 7 == 0 and num % 5 != 0:
        result_list.append(num)
    num += 1
print(f"divisible by 7 but not multible of 5 are: {[num for num in result_list]}")
