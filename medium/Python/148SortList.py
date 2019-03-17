# 使用归并排序(时间复杂度nlog(n))，使用递归来实现
# 不断二分为更小的链表，直到元素只有1，可以直接排序，然后把小的链表合并
# 写完后居然只有一个最大的元素被返回，错误原因，没有在merge函数中更新返回链表的节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head and head.next):
            dummyNode, dummyNode.next = ListNode(0), head
            slow, fast = dummyNode, dummyNode
            while(fast.next and fast.next.next):
                slow = slow.next
                fast = fast.next.next
            mid1, mid2 = head, slow.next
            slow.next = None
            mid1 = self.sortList(mid1)
            mid2 = self.sortList(mid2)
            return self.merge(mid1, mid2)
        else:
            return head

        
    def merge(self, l1, l2):
        dummyNode = ls = ListNode(0)
        while(l1 and l2):
            if l1.val < l2.val:
                ls.next = l1
                ls = ls.next
                l1 = l1.next
            else:
                ls.next = l2
                ls = ls.next
                l2 = l2.next
        if l1:
            ls.next = l1
        if l2:
            ls.next = l2
        return dummyNode.next