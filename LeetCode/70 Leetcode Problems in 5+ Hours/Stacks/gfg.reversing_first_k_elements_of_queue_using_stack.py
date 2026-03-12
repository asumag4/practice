# Given an integer k and a queue of integers, The task is to reverse the order of the first k elements of the queue, 
# leaving the other elements in the same relative order.

# Only following standard operations are allowed on the queue. 

#     enqueue(x): Add an item x to rear of queue
#     dequeue(): Remove an item from the front of the queue
#     size(): Returns the number of elements in the queue.
#     front(): Finds front item.

# Example:

#     Input: q = 1 2 3 4 5, k = 3
#     Output: 3 2 1 4 5
#     Explanation:  After reversing the first 3 elements from the given queue the resultant queue will be 3 2 1 4 5.

#     Input: q = 4 3 2 1, k= 4
#     Output: 1 2 3 4
#     Explanation: After reversing the first 4 elements from the given queue the resultant queue will be 1 2 3 4.

from collections import deque

class Solution:
    def reverseFirstKElements(self, q , k):

        def reverseAndAppendFirstK(q, k):
            q1 = deque()
            for _ in range(k):
                q1.appendleft(q.popleft())
            q.extend(q1)
            return q


        def organizeCorrectly(q, k): 
            s = len(q) - k
            for _ in range(s):
                n = q.popleft()
                q.append(n)
            return q

        q = deque(q)
        q = reverseAndAppendFirstK(q, k)
        q = organizeCorrectly(q, k)
        return q
    
sol = Solution()
print(sol.reverseFirstKElements([1,2,3,4,5], 3))
print(sol.reverseFirstKElements(q = [4,3,2,1], k = 4))