class Solution(object):
    def arrayRankTransform(self, arr):
        sor = list(sorted(set(arr)))
        res = []
        hmap = {}
        for i in range(len(sor)) :
            hmap[sor[i]] = i + 1
        for i in range(len(arr)) :
            res.append(hmap[arr[i]])
        return res
