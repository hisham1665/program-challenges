class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        map = {}
        for i in range(0 , len(s)):
            if s[i] in map:
                map[s[i]] = map[s[i]] + 1
            else : 
                map[s[i]] = 1
        for i in range(0 , len(s)):
            if t[i] in map :
                if map[t[i]] == 0 :
                    return False
                else :
                    map[t[i]] = map[t[i]] - 1
            else :
                return False
        return True
