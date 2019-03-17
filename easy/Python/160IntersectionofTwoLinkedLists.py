# 最基础的方法，直接遍历l1，每一个元素再与l2遍历的元素对比，第一个相同node的就是
# hhhhhhhh基础的方法果断超时了
# 方法一，两次遍历，第一次确定链表长度差，然后去掉差同步开始遍历
# 方法二，利用环的思想，做一次类似环的操作，然后两个遍历也就同步了

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         pa, pb = headA, headB
#         while(pa):
#             pb2 = pb
#             while(pb2):
#                 if pb2 == pa:
#                     return pb2
#                 else:
#                     pb2 = pb2.next
#             pa = pa.next
#         return None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB
        while(pa and pb):
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
                if(pa or pb):
                    if pa == None:
                        pa = headB
                    if pb == None:
                        pb = headA
                else:
                    break
        return None