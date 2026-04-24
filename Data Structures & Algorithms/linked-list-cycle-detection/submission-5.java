/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow=head;
        ListNode fast=head;
        if(head==null)return false;
        if (fast.next==null) return false;
        while(fast.next.next!=null && slow.next!=null ){

            slow=slow.next;
            fast=fast.next.next;
            if(fast.val==slow.val)return true;
            if(fast.next==null)return false;
        }
        return false;


    }
}
