#this is a program to find the valid parathesis problem in leetcode
s = input("enter the srring")
stack=[]
for i in range(len(s)):
    ch = s[i]
    if(ch == "(" or ch == "[" or ch=="{"):
        stack.append(ch)
    elif(len(stack) != 0 and ch == ")" and "(" in stack):
        stack.pop(stack.index("("))
    elif(len(stack) != 0 and ch == "]" and "[" in stack):
        stack.pop(stack.index("["))
    elif(len(stack) != 0 and ch == "}" and "{" in stack):
        stack.pop(stack.index("{"))
    else:
        print("false")
print("true")
        
