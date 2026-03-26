class Solution:
    def findMaxAverage(self, nums, k):
        # Step 1: first window ka sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: sliding window
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add new element
            window_sum -= nums[i-k]    # remove old element
            
            max_sum = max(max_sum, window_sum)

        # Step 3: average return
        return max_sum / k
        