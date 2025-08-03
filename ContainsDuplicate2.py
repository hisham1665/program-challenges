class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        ma = {}
        for i in range(len(nums)):
            if nums[i] in ma:
                if i - ma[nums[i]] <= k:
                    return True
            ma[nums[i]] = i
        return False
