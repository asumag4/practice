import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        nodes = []
        heapq.heapify(nodes)

        for x, y in points:
            euclidean = -((x*x) + (y*y))
            if (len(nodes) + 1 > k):
                heapq.heappushpop(nodes, (euclidean, x, y))
            else:
                heapq.heappush(nodes, (euclidean, x, y))

        return [[x,y] for euclidean, x, y in nodes]