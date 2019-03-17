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
        if head == None or head.next == None:
            return head
        
        cur = head.next
        pre = ListNode(head.val)

        while cur != None:
            newNode = ListNode(cur.val)
            newNode.next = pre
            pre = newNode
            cur = cur.next
        return newNode
        