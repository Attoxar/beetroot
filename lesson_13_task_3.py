def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        print("All numbers are positive, executing func1...")
        return func1(nums)
    else:
        print("Some numbers are negative, executing func2...")
        return func2(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


# print("Result for nums1:", choose_func(nums1, square_nums, remove_negatives))
# print("Result for nums2:", choose_func(nums2, square_nums, remove_negatives))


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
