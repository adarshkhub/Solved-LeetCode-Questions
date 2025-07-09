#Contains Duplicate

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# this should be simple with a hashset

# what i'm trying to do is if the value is not in the hashset already, add it to the set, else return true
nums = [1,3,4,5,1]

def containsDuplicate():
    store = set()
    for i in nums:
        if i in store:
            return True
        store.add(i)
    return i != i in nums


print(containsDuplicate())

