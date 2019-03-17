# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 就是一个逐步把.next的指针改变方向的操作
        reverse = None
        while head:
            nex = head.next
            head.next = reverse
            reverse = head
            head = nex
        return reverse