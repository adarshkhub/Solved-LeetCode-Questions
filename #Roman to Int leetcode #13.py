#Roman to Int leetcode #13



# first create a dictionary for each roman integer value

roman = {"I": 1,
"V" : 5,
"X" : 10,
"L" : 50,
"C" : 100,
"D" : 500,
"M" : 1000}

#1994
s = "XIV"
# i+1 < len(s) and 
def romanconversion(s):
    res = 0

    for i in range(len(s)):

        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]

        else:
            res += roman[s[i]]
    return res

print(romanconversion(s))

#if character value is less than the one following it, subtract
#if character value is greater than the one following it, add
#if character value is less than the one following it, substract, add it to total and then shift over 2 places