# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 这个方法超时。。。。。
# 还有一个bug不知道怎么能修改，就是不能只用val来对比node是否相同
# 思路：用一个box装遍历时经历过的元素，box大小限制在k，然后边界条件是是否碰到了None
# class Solution:
#     def rotateRight(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         if head == None or k < 1:
#             return head
#         box = ListNode(head.val)
#         p_box = box
#         count = 1
#         p = head
#         while(head.next):
#             if p.next:
#                 p = p.next
#                 if count < k:
#                     p_box.next = ListNode(p.val)
#                     p_box = p_box.next
#                     count += 1
#                 else:
#                     p_box.next = ListNode(p.val)
#                     p_box = p_box.next                    
#                     box = box.next
#             else:
#                 if count < k:
#                     k -= count + 1
#                     count = 0
#                     box = ListNode(head.val)
#                     p_box = box
#                     p = head
#                 else:
#                     h = ListNode(0)
#                     h.next = head
#                     if h.next.val == box.val:
#                         head = None
#                     while(h.next.val != box.val):
#                         h = h.next
#                     h.next = None
#                     p_box.next = head
#                     head = box
#                     break
#         return head


# 先进行一次遍历，记录大小N，首位相连，在第(N-k%N)处断开即可
# 需要精简
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p, p.next, N = ListNode(0), head, 0
        while(p.next):
            N += 1
            p = p.next
        if N > 0:
            p.next = head
            p = p.next
            count = 1
            while(count < N-k%N):
                p = p.next
                count += 1
            head = p.next
            p.next = None
        return head



r = a = ListNode(1)
a.next = ListNode(2)
a = a.next
a.next = ListNode(3)
a = a.next
a.next = ListNode(4)
a = a.next
a.next = ListNode(5)
k = 1

s = Solution()
b = s.rotateRight(r, k)
for i in range(5):
    print(b.val)
    b = b.next
