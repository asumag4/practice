from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frq = Counter(nums)

        return sorted(frq, key=lambda x: frq[x], reverse=True)[:k]