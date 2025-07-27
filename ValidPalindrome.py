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
