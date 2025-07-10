length = int(input("Enter the length: "))
a = []

print("Enter the elements:")
for i in range(length):
    a.append(int(input()))

target = int(input("Enter the target: "))
map = {}

for i in range(len(a)):
    complement = target - a[i]
    if complement in map:
        print("Indices:", map[complement], i)
        break
    else:
        map[a[i]] = i
