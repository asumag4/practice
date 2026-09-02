class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        counter = 0
        n = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                counter += min(tickets[i], n)
            else:
                counter += min(tickets[i], n - 1)
        return counter