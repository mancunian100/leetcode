# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        cur = l
        cur1 = l1
        cur2 = l2
        
        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
                
            cur = cur.next
        
        if cur1 or cur2:
            cur.next = cur1 or cur2
         
        return l.next