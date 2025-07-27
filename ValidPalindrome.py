#This is a leet code problem for find valid palindrome or not
#leetcode problem no : 125
def isPalindrome(s):
        filtered = ""
        for ch in s:
            if ch.isalnum():
                filtered += ch.lower()
        if(filtered == filtered[::-1]):
            return True
        else:
            return False

st = input("enter a string ")
print(isPalindrome(st))
