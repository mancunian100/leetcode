# 基本方法：直接转换成数字计算

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = n2 = 0
        lSum = None
        while(l1):
            n1 *= 10
            n1 += l1.val
            l1 = l1.next
        while(l2):
            n2 *= 10
            n2 += l2.val
            l2 = l2.next
        nSum = n1 + n2
        if nSum == 0:
            return ListNode(0)
        while(nSum):
            s = ListNode(nSum % 10)
            s.next = lSum
            lSum = s
            nSum //= 10
        return lSum