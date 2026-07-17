#leetcode problem no 643
class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum / float(k)
