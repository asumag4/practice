# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # # Base case
        # if (head.val == n):
        #     return None
        # if (not head):
        #     return None

        # 1. Traverse the whole list
        nodes_len = 0
        node = head
        while (node):
            if (not node):
                break
            node = node.next
            nodes_len += 1

        # Address base cases here
        if (nodes_len == 1):
            return None

        # 2. Traverse to position
        n_node_from_end = nodes_len - n
        node = head
        prev = head
        for _ in range(0,n_node_from_end):
            prev = node
            node = node.next
        # print(n_node_from_end)          # DEBUG
        # print(node)                     # DEBUG

        # 3. Replace n(i-1) -> n(i+1)
        if (n_node_from_end == 0):
            return head.next

        prev.next = node.next

        return head

            