# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 从中间开始翻转后半段的链表，与前半段对比
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = self.reverseList(slow)
        while mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True
        
        
    def reverseList(self, cur):
        pre = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre