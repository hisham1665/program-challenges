#this is program to perform binary addiiton
#leetcode problem no: 67
def addBinary(self, a, b):
        sum = int(a,2) + int(b,2)
        return bin(sum)[2:]
        
