#this is leet code problem solution
#leet code problem no : 206
#----------soloution---------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return head
        pre = None
        cur = head
        nex = cur.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nex
            if nex:
                nex = cur.next
        head = pre
        return head
