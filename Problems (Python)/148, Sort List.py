# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if head is None:
            return None

        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        arr.sort()

        l, r = head, 0

        while l:
            l.val = arr[r]
            r += 1
            l = l.next

        return head