def singleNumber(nums):
        result = 0
        for i in nums:
            result ^= i
        return result
nums = [4,1,2,1,2]
print(singleNumber(nums))
