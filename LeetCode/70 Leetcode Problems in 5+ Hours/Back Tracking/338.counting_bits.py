class Solution:
    def countBits(self, n: int) -> list[int]:

        # binary = [1,1,1]

        # if (len(binary) > 1):
        #     binary[1:len(binary)] = [0] * (len(binary) - 1)

        binary = [0]
        res = [0]
        b = 0

        for _ in range(1,n+1):

            if (0 not in binary):
                if (len(binary) > 1):
                    binary[1:len(binary)] = [0] * (len(binary) - 1)

                binary.append(0)
                res.append(sum(binary))
                print(binary)
                continue
            
            for idx, i in enumerate(binary[::-1]):
                if (i == 0):
                    binary[len(binary) - idx - 1] = 1
                    break
            
            print(binary)
            res.append(sum(binary))

        return res

sol = Solution()
print(sol.countBits(7))
            