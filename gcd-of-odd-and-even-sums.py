class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sumodd = n * n
        sumeven = n*(n+1)
        num = n
        for i in range(n  , 0):
            if sumodd % i == 0 and sumeven % i == 0 :
                num = i
                break
            else : 
                num = i - 1
        return num 
