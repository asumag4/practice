class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # insert = matrix[0]
        # insert.reverse()
        # return insert
        output = []
        action = 'l'

        while (len(matrix) >= 1): 
            
            # Left
            if action == 'l':
                insert = matrix.pop(0)
                output.extend(insert)
                action = 'd'
                continue

            # Down
            if action == 'd':
                insert = []
                for i in range(0, len(matrix)):
                    insert.append(matrix[i].pop())
                output.extend(insert)
                action = 'r'
                continue

            # Right
            if action == 'r':
                insert = matrix.pop(-1)
                insert.reverse()
                # print(insert)
                output.extend(insert)
                action = 'u'
                continue

            # Up
            if action == 'u':
                insert = []
                for i in range(0, len(matrix)):
                    insert.append(matrix[i].pop(0))
                insert.reverse()
                output.extend(insert)
                action = 'l'
                continue

        return output

sol = Solution()

print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]