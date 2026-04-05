# Beats 100%

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        
        start = points[0]
        counter = 0

        for i in points[1:]:
            
            # print(f"Starting point: {start}")
            # print(f"Current point: {i}")
            # print(f"Total moves: {counter}")

            delta_x = abs(start[0] - i[0])
            delta_y = abs(start[1] - i[1])
            # print(f"Delta X: {delta_x}")
            # print(f"Delta Y: {delta_y}")

            if (delta_x == delta_y):
                counter += delta_x
                # print(f"Sum of moves: {delta_x}")
            
            elif (delta_x < delta_y):
                delta_y -= delta_x
                counter += delta_x + delta_y
                # print(f"Sum of moves: {delta_x + delta_y}")
            
            else: 
                delta_x -= delta_y
                counter += delta_x + delta_y 
                # print(f"Sum of moves: {delta_x + delta_y}")
            
            start = i
        
        return counter

sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])) # 7 
print(sol.minTimeToVisitAllPoints([[3,2],[-2,2]]))