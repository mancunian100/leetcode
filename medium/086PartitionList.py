# 一开始认为并不需要设置sentinel，但是写着就发现需要了，总结一下需要的条件


# 错误的方法，本来希望可以直接改动head，似乎不行
# class Solution:
#     def partition(self, head, x):
#         """
#         :type head: ListNode
#         :type x: int
#         :rtype: ListNode
#         """
#         p, p.next = ListNode(0), head
#         les = p
#         while(p.next):
#             if p.next.val >= x:
#                 p = p.next
#             else:
#                 p_temp = p.next
#                 les_temp = les.next
#                 p.next = p.next.next
#                 les.next = p_temp
#                 les = les.next
#                 les.next = les_temp
#         return head

# 分开两个list存储，最后合并
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        s = smaller = ListNode(0)
        b = bigger = ListNode(0)
        while(head):
            if head.val >= x:
                bigger.next = ListNode(head.val)
                head, bigger = head.next, bigger.next
            else:
                smaller.next = ListNode(head.val)
                head, smaller = head.next, smaller.next
        smaller.next = b.next
        return s.next