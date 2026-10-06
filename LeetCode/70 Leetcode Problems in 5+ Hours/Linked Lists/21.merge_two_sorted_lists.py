# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        a = 0
        b = 0

        dummy = ListNode()
        clone = dummy

        # Compare at each position
        while (list1 and list2):

            if (list1.val < list2.val):
                clone.next = list1
                list1 = list1.next
            else:
                clone.next = list2
                list2 = list2.next
            
            clone = clone.next
        
        # Leftovers
        if (list1):
            clone.next = list1
        else:
            clone.next = list2

        return dummy.next