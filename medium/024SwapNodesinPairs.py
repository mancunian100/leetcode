# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 先交换元素，然后2个指针移动2个位置，循环，判断条件为后面是否有两个元素
# 记住while的bool条件传入方法这里的知识点
# 还是用了很繁琐的方法，应该把两个相同的步骤合到一起
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        sentinel = temp = ListNode(0)
        sentinel.next = head
        p1, p2 = head, head.next
        if p2 == None:
            return sentinel.next
        else:
            p1.next = p2.next
            p2.next = p1
            sentinel.next = p2
            if p1.next == None:
                return sentinel.next
            else:
                temp = p1
                p1 = p1.next
                p2 = p1.next
            while(p1 or p2):
                if p2 == None:
                    return sentinel.next
                else:
                    p1.next = p2.next
                    p2.next = p1
                    temp.next = p2
                    if p1.next:
                        temp = p1
                        p1 = p1.next
                        p2 = p1.next
                    else:
                        return sentinel.next

# 好了，两步合到一起了
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        sentinel = temp = ListNode(0)
        sentinel.next = head
        p1, p2 = head, head.next
        if p2 == None:
            return sentinel.next
        else:
            while(p1 or p2):
                if p2 == None:
                    return sentinel.next
                else:
                    p1.next = p2.next
                    p2.next = p1
                    temp.next = p2
                    if p1.next:
                        temp = p1
                        p1 = p1.next
                        p2 = p1.next
                    else:
                        return sentinel.next

# 还可以进一步整合 （36ms自己最快的方法，但是再精简就会变慢）
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        sentinel = temp = ListNode(0)
        sentinel.next = head
        p1 = head
        while(p1.next):
            p2 = p1.next
            p1.next = p2.next
            p2.next = p1
            temp.next = p2
            if p1.next:
                temp = p1
                p1 = p1.next
        return sentinel.next


# 自己的方法整理到最精简的形式
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = p1 = ListNode(0)
        sentinel.next = head
        while(p1.next and p1.next.next):
            p1, temp = p1.next, p1
            p2 = p1.next
            p1.next, p2.next, temp.next = p2.next, p1, p2
        return sentinel.next



# 借鉴了self作为sentinel的方法写出来的6行方法
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1, p1.next = self, head
        while(p1.next and p1.next.next):
            p1, temp = p1.next, p1
            p2 = p1.next
            p1.next, p2.next, temp.next = p2.next, p1, p2
        return self.next