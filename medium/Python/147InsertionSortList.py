# p指针遍历链表，每次都和head开始进行比较，若满足条件就插入，若到了p指针本身就不变

# 似乎还是因为没有完全搞懂python的深浅复制，现在还是对链表的插入不能完全游刃有余
# 现在问题是问什么head不行dummyNode.next就可以？？？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode, dummyNode.next = ListNode(0), head
        p = dummyNode
        while(p.next):
            pSort = dummyNode
            while(pSort != p):
                if p.next.val > pSort.next.val:
                    pSort = pSort.next
                else:
                    break
            if pSort == p:
                p = p.next
            else:
                temp1 = p.next
                p.next = p.next.next
                temp2 = pSort.next
                pSort.next = temp1
                pSort.next.next = temp2
        return dummyNode.next

a = ListNode(4)
a.next = ListNode(2)
s = Solution()
b = s.insertionSortList(a)
print(a.next)