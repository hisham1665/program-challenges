# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        flag = 1
        temp = n
        prev = 0
        while flag == 1 and temp > 0:
            if isBadVersion(temp) and isBadVersion(temp-1) == False:
                return temp
            elif isBadVersion(temp):
                prev = temp
                temp = temp // 2
            else :
                temp = (temp + prev) // 2
