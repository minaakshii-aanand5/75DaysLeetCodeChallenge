class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            rob1, rob2 = 0, 0

            for money in arr:
                current = max(money + rob1, rob2)
                rob1 = rob2
                rob2 = current

            return rob2

        return max(
            helper(nums[:-1]),   # exclude last house
            helper(nums[1:])     # exclude first house
        )
        