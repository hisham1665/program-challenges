# leetcode problem 234 
# use Two Pointer algorithm to check for palindrome
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head == None:
            return True
        li = []
        current = head
        while current != None:
            li.append(current.val)
            current = current.next
        left = 0
        right = len(li) - 1
        while right > left:
            if(li[right] != li[left]):
                return False
            right -= 1
            left += 1 
        return True
