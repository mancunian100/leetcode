# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ini = pre = ListNode(0)
        pre.next = head
        cur = head
        while cur:
            if cur.val == val:  
                pre.next = cur.next
            else:       
                pre = pre.next
            cur = cur.next
        return ini.next
        
                
            
            
 
        