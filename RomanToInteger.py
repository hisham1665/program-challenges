#this is program to convert roman numbers to integers

map = {"I" : 1, "V" : 5 , "X" : 10 ,"L": 50, "C" : 100, "D" : 500, "M" : 1000  }
str = input("Enter the string")
result = 0
i=0
for i in range(len(str)-1):
    if(map.get(str[i]) >= map.get(str[i+1])):
        result += map.get(str[i])
    else:
        result -= map.get(str[i])
    i+=1
result+=map.get(str[-1])
print(result)
