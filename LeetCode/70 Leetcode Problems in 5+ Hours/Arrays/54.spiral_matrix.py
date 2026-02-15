class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        output = []
        output.extend(matrix[0])

        x_len = len(matrix[0]) - 1

        output.extend([i[-1] for i in matrix[1:]])
        y_len = len(matrix)

        for i in range(1,y_len):
            print(y_len - i)

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))