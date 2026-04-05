class Solution:
    def climbStairs(self, n: int) -> int:
        
        seq = [0,1,2] 

        a = 1
        b = 2

        if n <= 2:
            return seq[n]

        for i in range(2,n+1):

            n_i = seq[a] + seq[b]
            seq.append(n_i)
            a += 1
            b += 1

        return seq[n]