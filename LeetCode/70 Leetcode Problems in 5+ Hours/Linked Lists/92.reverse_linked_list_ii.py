# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Base Case 
        if ((head == 0) or (left == right)):
            return head

        # If not base case:
        dummy = ListNode(val = 0)
        dummy.next = head
        prev = dummy

        # Go all the way to the left 
        for _ in range(left - 1):
            prev = prev.next

        # ==== Start shifts ====
        
        # For in range(0 , right - left)
        curr = prev.next
        for _ in range(0, right - left):
            after = curr.next
            curr.next = after.next
            after.next = prev.next
            prev.next = after

        return dummy.next


