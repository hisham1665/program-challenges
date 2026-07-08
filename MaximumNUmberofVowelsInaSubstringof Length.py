#leetcode problem no 1456
class Solution(object):
    def maxVowels(self, s, k):
        left = 0
        vow = {'a' , 'e' , 'i' ,'o' , 'u'}
        right = k
        count = 0
        for i in s[left:right]:
            if i in vow :
                count += 1
        maxc = count
        for right in range(k,len(s)):
            if s[left] in vow :
                count -= 1
            left += 1
            if s[right] in vow :
                count += 1
            if count > maxc :
                maxc = count
        return maxc

        
