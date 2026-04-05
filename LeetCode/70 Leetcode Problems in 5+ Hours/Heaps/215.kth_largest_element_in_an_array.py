import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        # We'll use heaps
        # Init an empty list to store our heaps 
        nodes = []
        heapq.heapify(nodes)

        # You want to build the heap upwards -> biggest to smallest
        for num in nums:
            heapq.heappush(nodes, num)

        # Whenever the length of heap gets bigger than k        
            if (len(nodes) > k):
                # Pop the smallest element from heap
                heapq.heappop(nodes)

        return heapq.heappop(nodes)
        
