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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode dummy = new ListNode();
        ListNode clone = dummy;

        while ((list1 != null) && (list2 != null)) {

            if (list1.val < list2.val) {
                clone.next = list1;
                list1 = list1.next;
            } else {
                clone.next = list2;
                list2 = list2.next;
            }

            clone = clone.next;

        } 

        if (list1 != null) {
            clone.next = list1;
        } else {
            clone.next = list2;
        }

        return dummy.next;

    }
}