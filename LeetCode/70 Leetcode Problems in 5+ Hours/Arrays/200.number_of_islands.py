from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        res = 0
        traversed = set()
        c_len, r_len = len(grid), len(grid[0])

        def bfs(c,r):
            q = deque([(c,r)])
            traversed.add((c,r))

            while q:

                col, row = q.popleft()

                for d_c, d_r in [(-1,0),(0,-1),(1,0),(0,1)]:
                    
                    n_c = d_c + col
                    n_r = d_r + row

                    if (
                        (0 <= n_c < c_len) and 
                        (0 <= n_r < r_len) and 
                        (grid[n_c][n_r] == "1") and 
                        ((n_c,n_r) not in traversed)
                    ):
                        q.append((n_c,n_r))
                        traversed.add((n_c,n_r))
            

        for c in range(0,c_len):
            for r in range(0,r_len):
                if ((grid[c][r] == "1") and 
                ((c,r) not in traversed)
                ):
                    res += 1
                    bfs(c,r)
        
        return res
sol = Solution()
print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # 1
# print(sol.numIslands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ])) # 3