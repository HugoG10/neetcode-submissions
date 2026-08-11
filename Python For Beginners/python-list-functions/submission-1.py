from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total = 0
    for num in nums:
        total += num

    return total

def get_min(nums: List[int]) -> int:
    min_num = nums[0]
    for i in range(len(nums)):
        if i == len(nums) - 1:
            break
        if min_num > nums[i]:
            if nums[i] < nums[i + 1]:
                min_num = nums[i]

    return min_num

def get_max(nums: List[int]) -> int:
    max_num = nums[0]

    for i in range(len(nums)):
        if i == len(nums) - 1:
            break
        if max_num < nums[i + 1]:
            if nums[i] < nums[i + 1]:
                max_num = nums[i + 1]

    return max_num

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
