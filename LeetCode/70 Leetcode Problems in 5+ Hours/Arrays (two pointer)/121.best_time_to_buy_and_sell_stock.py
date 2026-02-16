class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # Initiate starting points of 2 pointer solution
        left = 0
        right = 0
        best_price = 0

        while (right <= (len(prices) - 1)):

            if prices[left] > prices[right]:
                left = right
                right += 1
            else: 
                if ((prices[right] - prices[left]) > best_price):
                    best_price = prices[right] - prices[left]
                right += 1

            # print(prices[left], prices[right])
        
        return best_price

    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])) # 5
print(sol.maxProfit([7,6,4,3,1])) # 0
print(sol.maxProfit([1,2])) # 0
