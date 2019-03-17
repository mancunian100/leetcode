# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 思路与024基本一样，循环，边界条件是看是否有足够需要交换的元素
# 这里的技巧是用一个pk容器保存中间的k个元素，一边保存一边交换顺序，满足数量就接上之前留下的头和尾
# 注意要记得break
# 注意衔接尾部时的记清楚之前有更新，用更新后的指针
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head
        sentinel, sentinel.next = ListNode(0), head
        p = temp = sentinel
        while(p.next):
            count = 1
            p = p.next
            pk = ListNode(p.val)
            while(p.next):
                p = p.next
                pk_pre = pk
                pk = ListNode(p.val)
                pk.next = pk_pre
                count += 1
                if count == k:
                    temp.next = pk
                    p_temp = pk
                    while(p_temp.next):
                        p_temp = p_temp.next
                    p_temp.next = p.next
                    temp = p_temp
                    break
        return sentinel.next

# r = a = ListNode(1)
# a.next = ListNode(2)
# a = a.next
# a.next = ListNode(3)
# a = a.next
# a.next = ListNode(4)
# a = a.next
# a.next = ListNode(5)

# b = Solution()
# c = b.reverseKGroup(r, 2)
# for i in range(5):
#     print(c.val)
#     c = c.next