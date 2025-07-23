#this is the leet code problem number 83
# remove duplicates form sorted list
# this is the leetcode solution below

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while (current and current.next):
            if (current.val == current.next.val):
                current.next = current.next.next
            else:
                current = current.next
        return head


# to remove the duplicates in a list is given below:
# a = input("enter the array ")
# b = [int(x) for x in a.split()]
# c = list(set(b))
# print(c)
