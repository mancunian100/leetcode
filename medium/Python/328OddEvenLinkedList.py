# 使用两个指针

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode, dummyNode.next = ListNode(0), head
        if(head and head.next):
            pOdd = head
            pEven = head.next
        else:
            return head
        while(pEven.next and pEven.next.next):
            temp1 = pOdd.next
            temp2 = pEven.next.next
            pOdd.next = pEven.next
            pOdd.next.next = temp1
            pEven.next = temp2
            pEven = pEven.next
            pOdd = pOdd.next
        if pEven.next:
            temp = pOdd.next
            pOdd.next = pEven.next
            pOdd.next.next = temp
            pEven.next = None
        return head

