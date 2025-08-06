#2sum with hashmap


nums = [2,7,11,15]

target = 9

def twoSum(nums, target):

    legend = {}


    for i, j in enumerate(nums):
        k = target - j
        if k in legend:
            return [legend[k], i]
        legend[j] = i


print(twoSum(nums, target))