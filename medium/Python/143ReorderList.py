# naive想法：指针往前走，每遇到一个就插在record的root节点的后面
# 题目看错了，没注意下标的细节，以后看题要小心下标这样的细节了
# 自己没有想出方法，看了别人答案
# 首先找到链表的中间节点（方法是使用快慢指针），然后翻转后一半链表，然后把两段链表交叉连接
# 本来想用dummyNode，但是发现还是不能简单统一所有情况，反而需要加入更多的分支，
# 还是直接开头if判断是否有3个元素比较方便

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            slow = fast = head
            while(fast.next and fast.next.next):
                slow = slow.next
                fast = fast.next.next
            pRev, reverseHalf = slow.next, None
            while(pRev):
                temp = pRev.next
                pRev.next = reverseHalf
                reverseHalf = pRev
                pRev = temp
            p1, p2 = head, reverseHalf
            slow.next = None
            while(p1 and p2):
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p1 = p2.next = temp1
                p2 = temp2