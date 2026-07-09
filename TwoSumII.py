class Solution(object):
    def twoSum(self, numbers, target):
        hmap = {}
        for i in range(len(numbers)) :
            comp = target - numbers[i]
            if comp in hmap :
                return [hmap[comp] + 1 , i + 1]
            else :
                hmap[numbers[i]] = i

