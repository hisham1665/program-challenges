# leetcode problem no 11
class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height) - 1
        hi , max = 0 , 0
        while left < right :
            if height[right] > height[left]:
                hi = height[left] * (right - left)
                left+= 1
            else :
                hi = height[right] * (right - left)
                right -= 1
            if max < hi:
                max = hi
        return max

        
