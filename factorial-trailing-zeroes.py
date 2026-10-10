class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum = 0
        while n >= 5:
            n = n // 5
            sum = sum + n
        return sum
