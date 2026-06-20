#kadanes algorithm

class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        big = current
        for i in range(1,len(nums)):
            if current + nums[i] > nums[i] :
                current += nums[i]
            else :
                current = nums[i]
            if big < current :
                big = current
        return big
