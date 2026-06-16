class Solution(object):
    def firstUniqChar(self, s):
        hmap = {}
        for i in range(0,len(s)) :
            if s[i] in hmap:
                hmap[s[i]] = -1
            else :
                hmap[s[i]] = i
        val = [v for v in hmap.values() if v >= 0 ]
        return min(val) if val else -1

        
