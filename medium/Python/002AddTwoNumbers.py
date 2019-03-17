# Definition for singly-linked list
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

##############
### extremely naive solution. without the "carry" counter, 
### the "p3.next" is repeatly utilized to implement the carry function

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         result = ListNode(0)
#         p1 = l1
#         p2 = l2
#         p3 = result
#         while(p1 != None and p2 != None):
#             if p3.next == None:
#                 p3.next = ListNode(0)
#             p3 = p3.next
#             p3.val += p1.val + p2.val
#             if p3.val > 9:
#                 p3.next = ListNode(p3.val // 10)
#                 p3.val %= 10
#             p1 = p1.next
#             p2 = p2.next
#         if(p1 == None and p2 != None):
#             if p3.next == None:
#                 p3.next = ListNode(0)
#             p3 = p3.next
#             p3.val += p2.val
#             while(p3.val > 9):
#                 if p2.next != None:
#                     p3.next = ListNode(p3.val // 10 + p2.next.val)
#                 else:
#                     p3.next = ListNode(p3.val // 10)
#                 p3.val %= 10
#                 p2 = p2.next
#                 p3 = p3.next
#             if p2 != None:
#                 p3.next = p2.next
            
#         elif(p1 != None and p2 == None):
#             if p3.next == None:
#                 p3.next = ListNode(0)
#             p3 = p3.next
#             p3.val += p1.val
#             while(p3.val > 9):
#                 if p1.next != None:
#                     p3.next = ListNode(p3.val // 10 + p1.next.val)
#                 else:
#                     p3.next = ListNode(p3.val // 10)
#                 p3.val %= 10
#                 p1 = p1.next
#                 p3 = p3.next
#             if p1 != None:
#                 p3.next = p1.next
#         return result.next

###########
# clean and beautiful solution

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = result = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            v = v1 + v2 + carry
            p.next = ListNode(v % 10)
            carry = v // 10
            p = p.next
        return result.next
            