#leetcode no 3
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hmap = set()
        right = -1
        left = maxsize = 0
        for i in s :
            if i in hmap :
                if s[left] == i:
                    left += 1
                else :
                    while s[left] != i:
                        hmap.discard(s[left])
                        left+= 1
                    left += 1
                right += 1
            else : 
                right += 1
                if (right - left) + 1 > maxsize :
                    maxsize = (right - left) + 1
                hmap.add(i)
        return maxsize        
