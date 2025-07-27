#this is program to solve Plus One Problem in leet code
#leet code problem no : 66
def plusOne( digits):
        n = len(digits)
        for i in range(n-1 , -1 ,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        res = [1] + digits
        return res 
st = input("Enter the digits")
digits = [int(i) for i in st.split()]
print(plusOne(digits))
