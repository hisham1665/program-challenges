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
        

# another solution
class Solution(object):
    def numberGame(self, nums):
        nums = sorted(nums)
        k = j = -1
        while k < len(nums) -2:
            k = j + 1
            j = k+1
            nums[k] = nums[k] + nums[j]
            nums[j] = nums[k] - nums[j]
            nums[k] = nums[k] - nums[j]
        return nums
