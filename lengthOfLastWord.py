a = input("enter a string : ")
b = a.strip().split(" ")
last_word = b[len(b) - 1]
print(len(last_word))
