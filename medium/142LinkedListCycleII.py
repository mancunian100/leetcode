# 快慢两个指针，相遇后快的回到head并每次也只前进一步，再次相遇即为cycle的开始node
# 直接看了别人的结论，虽然能够推导但是不知道为什么这样解，如果忘记方法那就不会从头推导了
# 似乎还不理解为什么slow还要在重置时前进一步

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode, dummyNode.next = ListNode(0), head
        fast = slow = dummyNode
        while(slow.next and fast.next and fast.next.next):
            if slow.next == fast.next.next:
                slow = slow.next
                fast = dummyNode
                while(slow.next != fast.next):
                    slow = slow.next
                    fast = fast.next
                return slow.next
            else:
                slow = slow.next
                fast = fast.next.next
        return None