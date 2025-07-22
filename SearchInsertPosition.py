def searchInsert(nums , target):
  left = 0
  right = len(nums) - 1
  while(left <= right):
    mid = left + (right - left) // 2 
    if(nums[mid] == target):
      return mid
    elif(target < nums[mid]):
      right = mid - 1
    else:
      left = mid + 1
  return left

array = input("enter the nums : ")
nums = [int(x) for x in array.split()]
target = int(input("enter the target: "))

result = searchInsert(nums , target)
print(f"The target should be inserted at index: {result}")
