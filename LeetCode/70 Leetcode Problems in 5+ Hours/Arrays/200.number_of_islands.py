class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        dummy = [[0] * len(grid[0]) for i in range(0,len(grid))]
        counter = 0
        x_end = len(grid[0]) - 1
        y_end = len(grid) - 1 

        def traverse(x,y):
            global counter 

            if ((x == x_end) and (y == y_end)):
                return
            
            while x <= x_end:
                x += 1

                if grid[y][x] == 1:
                    dummy[y][x] == counter 
                    left = traverse(x+1,y)
                    bottom = traverse(x,y+1)
                    
                if (left or bottom):
                    return True
                else:
                    counter += 1
                    return False
        
        traverse(0,0)
        print(dummy)
        

sol = Solution()
print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))