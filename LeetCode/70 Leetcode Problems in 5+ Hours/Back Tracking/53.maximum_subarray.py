class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Start at a = 0 and b = 0 for the case of when there's only one item in the list
        a = 0
        b = 0
        # Grab only from one position because we don't want to res = nums[0] * 2
        res = nums[a] 
        curr = res

        # Need to make this recursive: 
        # need to assess between the current iteration vs. the proposed push
        def push(jab, pivot, contend):
            if (jab )
            return sum(nums[n_a, n_b + 1])

        # We'll use a Greedy Approach, assess += 1 for a or b, go towards the step that increases (+) the most
        while (
            # Placement conditionals
            (b <= len(nums) - 1) and 
            (a <= b) and
            # sum-based conditionals
            ):
            
            if ((a + 1) <= b):
                a_push = push(a+1, b)
            if (b <= len(nums)):
                b_push = push(a, b+1)
            
            if (a_push > b_push):
                a += 1
                res = max(res, a_push)
            else:
                b += 1
                res = max(res, b_push)

            # But if the += 1 step for either a or b is smaller than the current number,

            # Look at traversing first on the largest number