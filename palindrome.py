#this is a program to check the given number is pallindrome or not
def checkPalindrome(num):
    left = 0
    right = len(num)-1
    while (left < right):
        if(num[left] != num[right]):
            return False
        left+=1
        right-=1
    return True
num = input("Enter the number")
result = checkPalindrome(num)
print("Result : "+ str(result))
