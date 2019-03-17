# 利用两个快慢指针，若有cycle必然两指针会相遇(之前不知道链表也可以判断是否相等)

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, slow.next = ListNode(0), head
        fast = slow
        while(slow.next and fast.next and fast.next.next):
            if slow.next == fast.next.next:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False