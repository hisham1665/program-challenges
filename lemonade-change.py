# leetcode no 860
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        hmap = {'5' : 0 , '10' : 0 , '20' : 0}
        for i in bills :
            if i == 5 :
                hmap['5'] += 1
            elif i == 10 :
                if hmap['5'] != 0:
                    hmap['10'] += 1
                    hmap['5'] -= 1
                else :
                    return False
            else :
                if hmap['5'] != 0 and hmap['10'] != 0:
                    hmap['20'] += 1
                    hmap['5'] -= 1
                    hmap['10'] -= 1
                elif hmap['5'] >= 3:
                    hmap['20'] += 1
                    hmap['5'] -= 3
                else :
                    return False
        return True
