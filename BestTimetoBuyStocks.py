# this is a program to solve the leet code problem of best time to buy and sell stocks
#leetcode problem number 121
prices = [7 , 1  , 5 , 3 , 6 , 4]
max_profit = 0
minimum = prices[0]
for i in prices:
  minimum = min(minimum , i)
  profit = i - minimum
  max_profit = max(max_profit , profit)
print(max_profit)
