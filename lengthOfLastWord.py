#this is a program to find the number of charecters of the last word 
a = input("enter a string : ")
b = a.strip().split(" ")
last_word = b[len(b) - 1]
print(len(last_word))
