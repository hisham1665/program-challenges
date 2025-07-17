count = int(input("Enter the number of words: "))
strs = []
for i in range(count):
    item = input("Enter word {}: ".format(i + 1))
    strs.append(item)
def longest_common_prefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]
prefix = longest_common_prefix(strs)
print("Longest common prefix:", prefix if prefix else "No common prefix")
