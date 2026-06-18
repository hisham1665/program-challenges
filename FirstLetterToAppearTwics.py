# Problem no 2351 in leetcode

class Solution(object):
    def repeatedCharacter(self, s):
        hmap = {}
        for i , char in enumerate(s):
            if char in hmap:
                hmap[char] = hmap[char] + 1
                if hmap[char] == 2:
                    return char
            else:
                hmap[char] = 1
