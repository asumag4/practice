class Solution:
    def countBits(self, n: int) -> list[int]:
        
        # Initiate a holder list 
        bin_combos = ["0", "1"]
        stage = 2

        while stage <= n:
            ext_combos = []
            
            # Develop
            stage *= 2
            for i in bin_combos:
                bin_rep = "1" + str(i)
                ext_combos.append(str(bin_rep))         

            bin_combos.extend(ext_combos)   

        # print(bin_combos) # DEBUG
                
        res = []
        for bit in bin_combos[0:n+1]:
            bit = [int(idx) for idx in list(bit)]
            res.append(sum(bit))

        return res

sol = Solution()
print(sol.countBits(5))
            