class Solution {
    public int maxSubArray(int[] nums) {
        // declare the current sum and maxsum
        int sum = nums[0], maxSum = sum;
        // iterate through the list
        for (int i = 1; i < nums.length; i++) {
            // incr sum on i 
            sum += nums[i];
            // assess if sum is greater than maxsum
            maxSum = Math.max(maxSum, sum);

            // assess if sum is less than i
            if (sum < nums[i]) {
                // if so; reset sum to i
                sum = nums[i];
                // and make sure to check if the maxsum is less than sum now
                maxSum = Math.max(maxSum, sum);
            }
        }

        return maxSum;

    }
}