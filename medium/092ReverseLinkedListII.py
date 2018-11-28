# 当移动到要反转的范围时用reverse临时保存，最后出来时插进去
# 和easy的反转链表一样，我还没有完全掌握python的复制引用的规律
# 这里还要注意要使用前置的dummyNode作为返回值
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p, p.next = ListNode(0), head
        dummyNode = p
        reverse = None
        count = 0
        while(p.next):
            count += 1
            if count >= m:
                temp = p.next.next
                p.next.next = reverse
                reverse = p.next
                p.next = temp
                if count == n:
                    tail = p.next
                    p.next = reverse
                    while(p.next):
                        p = p.next
                    p.next = tail
                    break
            else:
                p = p.next
        return dummyNode.next