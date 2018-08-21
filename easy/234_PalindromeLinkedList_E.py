# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 先倒置head，倒置后与head相同则为True, 慢，击败10%
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        
        cur = head.next
        pre = ListNode(head.val)

        while cur != None:
            newNode = ListNode(cur.val)
            newNode.next = pre
            pre = newNode
            cur = cur.next
        
        cur = head
        while cur != None:
            if cur.val != newNode.val:
                return False
            cur = cur.next
            newNode = newNode.next

        return True
        

# 遍历head，存入list，判断list是否对称，快，98%
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        
        cur = head
        mylist = []
        while cur is not None:
            mylist.append(cur.val)
            cur = cur.next
        
        l = len(mylist)//2
        
        for i,j in zip(mylist[0:l], mylist[:-l-1:-1]):
            if i != j:
                return False
        return True
     
        
        
        
        
        