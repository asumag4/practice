class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        check = [amount + 1] * (amount + 1)
        check[0] = 0

        for i in range(0,len(check)):
            for c in coins:
                if ((i-c) >= 0):
                    check[i] = min(check[i], 1 + check[i-c])
        
        return check[amount] if (check[amount] != (amount + 1)) else -1


sol = Solution()
print(sol.coinChange(coins = [1,2,5], amount = 11)) # 3 for [5,5,1]
# print(sol.coinChange(coins = [2], amount = 3)) # 0
# print(sol.coinChange(coins = [1], amount = 0)) 