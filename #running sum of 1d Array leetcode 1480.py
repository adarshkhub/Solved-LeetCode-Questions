#running sum of 1d Array leetcode 1480


nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

store = 0
rsum = []
for i in range(len(nums)):
    store += nums[i]
    rsum.append(store)

print(rsum)