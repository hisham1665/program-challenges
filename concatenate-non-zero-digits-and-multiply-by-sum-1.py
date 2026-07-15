class Solution(object):
    def sumAndMultiply(self, n):
        num = n
        res = 0
        st = ""
        while num :
            val = num % 10
            if val != 0 :
                res = res * 10 + val
            num = num // 10
        sums = sum(list(map(int, str(res))))

        return int(str(abs(res))[::-1]) * sums 
