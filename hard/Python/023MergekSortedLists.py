# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 分治法，但是最后的处理需要两两处理，不能逐个处理，不然会超时，原因不明
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        else:
            l = len(lists)
            while(l-1):
                cap = (l+1)//2
                for i in range(0, l//2):
                    lists[i] = self.mergeSort(lists[i], lists[i+cap])
                l = cap
            # result = lists[0]
            return lists[0]
        
        
    def mergeSort(self, l1, l2):
        """
        :l1, l2: sorted lists
        :return: merged sorted listnode
        """
        if l1 == None and l2 == None:
            return None
        r = result = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                r.next = l1
                l1 = l1.next
                r = r.next
            else:
                r.next = l2
                l2 = l2.next
                r = r.next
        r.next = l1 if l1 else l2
        return result.next
            