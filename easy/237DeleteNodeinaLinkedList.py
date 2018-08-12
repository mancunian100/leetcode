# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 注意这里输入的node就是链表中那个需要删除的节点，所以直接对node操作
        node.val = node.next.val
        node.next = node.next.next