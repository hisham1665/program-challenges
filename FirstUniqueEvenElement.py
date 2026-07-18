#leetcode no 3866
class Solution(object):
    def firstUniqueEven(self, nums):
        hmap = {}
        for i , dig in enumerate(nums):
            if dig % 2 == 0:
                if dig in hmap:
                    hmap[dig] = -1
                else :
                    hmap[dig] = i
        val = [v for v in hmap.values() if v >= 0 ]
        return nums[min(val)] if val else -1
