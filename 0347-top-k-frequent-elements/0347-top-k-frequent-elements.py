class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        # Step 1: frequency count
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: sort based on frequency
        sorted_nums = sorted(count, key=count.get, reverse=True)

        # Step 3: return top k
        return sorted_nums[:k]