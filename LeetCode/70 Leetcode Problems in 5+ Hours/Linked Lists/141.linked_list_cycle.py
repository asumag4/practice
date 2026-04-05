# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        traversed = set()
        prev = None
        qloop = False

        node = head

        while (node):

            if ((node.val == prev) and (qloop == True)):
                print(f"Found loop @ {node.val}")
                return True
            
            if (node.val in traversed):
                prev = node.val
                print(prev)
                qloop = True
                
            traversed.add(node.val)
            node = node.next

        return False