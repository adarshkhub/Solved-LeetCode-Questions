#leetcode move zeroes

#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.


nums = [0,1,0,3,12]

# 2 pointer problem
#hint move all non zero elements to the left side of the array

def moveZeroes(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
    return nums



print(moveZeroes(nums))