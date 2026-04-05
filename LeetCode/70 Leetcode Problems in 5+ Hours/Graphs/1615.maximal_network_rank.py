from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        connected = defaultdict(int)
        for ai, bi in roads:
            connected[ai] += 1
            connected[bi] += 1
        
        maxNetwork = 0
        for ai in range(n):
            for bi in range(ai + 1, n):
                if ([ai, bi] in roads) or ([bi, ai] in roads):
                    maxNetwork = max(maxNetwork, connected[ai] + connected[bi] - 1)
                else:
                    print(ai, bi, connected[ai] + connected[bi])
                    maxNetwork = max(maxNetwork, connected[ai] + connected[bi])
        
        # print(connected)
        return maxNetwork