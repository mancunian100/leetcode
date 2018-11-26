# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 在判断重复元素后对链表的处理还有点懵比
        # if not head:
        #     return head
        # curIndex = head.next
        # curResult = head
        # while curIndex is not None:
        #     while curIndex.val == curResult.val:
        #         curIndex = curIndex.next
        #         curResult.next = curResult
        #         if curIndex is None:
        #             return head
        #     curIndex = curIndex.next
        #     curResult = curResult.next
        # return head

        # if not head:
        #     return head

        # cur = head
        # nex = head.next

        # while nex != None:
        #     while cur.val == nex.val:
        #         nex = nex.next
        #         cur.next = nex
        #         if nex == None:
        #             return head
        #     cur = cur.next
        #     nex = nex.next
        # return head

        # 精简后的代码，现在处理链表熟练多了
        if head:
            p = head
            while(p.next):
                if p.val != p.next.val:
                    p = p.next
                else:
                    p.next = p.next.next
        return head