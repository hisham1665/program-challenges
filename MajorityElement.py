#this is a leetcode problem of no : 16 (majority elements)
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        maj = None
        for i  in nums:
            if count == 0:
                maj = i
            count += (1 if i == maj else -1 )
        return maj
