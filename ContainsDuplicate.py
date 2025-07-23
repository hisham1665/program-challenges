# this is a leetcode problem of solving Contains Duplicate
# leetcode problem 217;
a = input("enter the array ")
b = [int(x) for x in a.split()]
c = list(set(b))
if len(c) < len(b):
  print(True)
else:
  print(False)
