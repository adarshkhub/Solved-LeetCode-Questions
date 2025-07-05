#leetcode plus one

# need to code for the case where the last number, or the last two numbers etc is 9
# can use a while loop to iterate backwards for cases while number is 9
# What would the base case be


digits = [4,3,9,9]

def plusOne(digits):


    if digits[-1] != 9:
        digits[-1] += 1

    if digits[-1] == 9:
        for i in range((len(digits)), -1, -1):
         k = -1
        while digits[k] == 9:
            digits[k] = 0
            if digits[k-1] < 9:
               digits[k-1] += 1
            k -= 1
        return digits 
    

print(plusOne(digits))
