# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 基本方法，注意在最前面加上哨兵元素保证第一个被去掉时可以实现
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        result = temp = ListNode(0)
        temp.next = head
        pn = 0
        while(p.next != None):
            p = p.next
            pn += 1
            if pn >= n:
                temp = temp.next
        if  pn == 0:
            return None
        temp.next = temp.next.next
        return result.next