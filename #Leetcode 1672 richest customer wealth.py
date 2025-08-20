#Leetcode 1672 richest customer wealth


#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.

#A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

#the highest sum = the richest customer

#print(sum(accounts[1])) works

accounts = [[1,2,3],[3,2,1],[2,1,1]]

#expected answer = 6


#Also try it with a dictionary
#create an array which stores the sums of each array in accounts
#return the highest value in that array

#for i in accounts:

j = 0
totals = []
k = 0

for i in accounts:
    totals.append(sum(accounts[j]))
    j+=1

for l in range(len(totals)):
    if k <= totals[l]:
        k = totals[l]

    
print(k) 




 