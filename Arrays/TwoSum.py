# Problem: Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return []
