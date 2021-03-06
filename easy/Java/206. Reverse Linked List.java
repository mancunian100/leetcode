package javaEasy;

/**
 * @author mancunian100.
 */

class Solution {
    public ListNode reverseList(ListNode head) {

        /** 插入到sentinel之后，第一个之前 */
//        ListNode sentinel = new ListNode(0);
//        sentinel.next = head;
//        ListNode p = head;
//
//        while (p != null && p.next != null) {
//            ListNode temp1 = p.next;
//            p.next = p.next.next;
//            ListNode temp2 = sentinel.next;
//            sentinel.next = temp1;
//            sentinel.next.next = temp2;
//        }
//
//        return sentinel.next;

        /** 逐个反转箭头指向 */
        ListNode reverse = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = reverse;
            reverse = head;
            head = temp;
        }
        return reverse;
    }

    public static void main(String[] args) {
        ListNode test = new ListNode(1);
        ListNode p = test;
        for (int i = 0; i < 4; i += 1) {
            p.next = new ListNode(i + 2);
            p = p.next;
        }

        ListNode pTest = test;
        while (pTest != null) {
            System.out.print(pTest.val + " ");
            pTest = pTest.next;
        }

        Solution s = new Solution();
        ListNode res = s.reverseList(test);
        while (res != null) {
            System.out.print(res.val + " ");
            res = res.next;
        }
    }
}
