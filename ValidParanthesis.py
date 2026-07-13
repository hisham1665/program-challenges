#this is a program to find the valid parathesis problem in leetcode
#leetcode problem 20
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            ch = s[i]
            if(ch == "(" or ch == "[" or ch=="{"):
                stack.append(ch)
            else :
                if not stack :
                    return False
                elif ch == ")" and stack[-1] != "(" :
                    return False
                elif ch == "]" and stack[-1] != "[":
                    return False
                elif ch == "}" and stack[-1] != "{":
                    return False
                else :
                    stack.pop()
        return len(stack) == 0
        
