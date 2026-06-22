class Solution(object):
    def numberGame(self, nums):
        nums = sorted(nums)
        k = j = -1
        out = []
        while k < len(nums) -2:
            k = j + 1
            j = k+1
            out.append(nums[j])
            out.append(nums[k])
        return out
        
