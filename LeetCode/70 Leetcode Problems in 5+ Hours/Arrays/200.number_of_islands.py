from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        traversed = []
        counter = 0  
        x_len = len(grid[0]) - 1
        y_len = len(grid) - 1

        def scopeIsland(x, y):

            q = deque([(x,y)])

            while q:
                
                print(q)
                n_x, n_y = q.popleft()

                for dir_x, dir_y in ([(-1,0), (0,1), (1,0), (0,-1)]):

                    if (n_x + dir_x, n_y + dir_y) in traversed:
                        continue
                    else: 
                        if (
                            n_x < x_len and
                            n_x > 0 and
                            n_y < y_len and
                            n_y > 0
                        ):
                            if (grid[n_x + dir_x][n_y + dir_y] == "1"):
                                q.append((n_x + dir_x, n_y + dir_y))
                            traversed.append((n_x + dir_x, n_y + dir_y))
            

        for x in range(0,len(grid)):
            for y in range(0, len(grid[0])):

                # print(grid[i][j])

                if (x,y) in traversed:
                    continue
                else:
                    if (grid[x][y] == "1"): 
                        # print("Found an island!")
                        counter += 1
                        scopeIsland(x,y)
                    else: 
                        traversed.append((x,y))

        return counter
        

sol = Solution()
print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # 1
print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # 3