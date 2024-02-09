# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-368. Largest Divisible Subset-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 09- 2024
# URL: https://leetcode.com/problems/largest-divisible-subset/
# ====================================================================

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # [1,  2,  3]
        # using a dfs starting from adding the first or not number lmao

        nums.sort()
        cache = {}

        def dfs(index):
            if index >= len(nums):
                return []
            
            if index in cache:
                return cache[index]

            current_subset = [nums[index]]

            for j in range(index + 1, len(nums)):
                if nums[j] % nums[index] == 0:
                    # Wecan addit
                    tmp = [nums[index]] + dfs(j)

                    if len(tmp)> len(current_subset):
                        current_subset = tmp

            cache[index] = current_subset
            return current_subset 


        largest = []

        for i in range(len(nums)):
            curr = dfs(i)
            if len(curr) > len(largest):
                largest = curr


        return largest