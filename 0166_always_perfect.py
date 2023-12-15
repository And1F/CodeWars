from math import sqrt

def check_root(string):
    nums = string.split(',')
    if len(nums) != 4 or not all(x.lstrip('-').isdigit() for x in nums):
        return 'incorrect input'
    if [int(x) for x in nums] != [int(nums[0]), int(nums[0]) + 1, int(nums[0]) + 2, int(nums[0]) + 3]:
        return "not consecutive"
    square = int(nums[0]) * int(nums[1]) * int(nums[2]) * int(nums[3]) + 1
    if sqrt(square).is_integer():
        return f'{square}, {int(sqrt(square))}'
    else:
        return "not a perfect square"