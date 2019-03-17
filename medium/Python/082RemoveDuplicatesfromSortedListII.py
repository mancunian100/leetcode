# 注意遇到重复数情况时和不重复时p的更新不一样，体现在continue的使用上
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, p.next = ListNode(0), head
        res = p
        while(p and p.next):
            temp = p.next
            if(temp.next):
                if(temp.val == temp.next.val):
                    while(temp.next and temp.val == temp.next.val):
                        temp = temp.next
                    p.next = temp.next
                    continue
            p = p.next
        return res.next