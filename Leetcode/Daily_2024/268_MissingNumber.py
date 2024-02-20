# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 268. Missing Number -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: February - 19- 2024
# URL:https://leetcode.com/problems/missing-number/
# ====================================================================

# [0, 1, 3]
# [0, 1, 2, 3] -> 3 + 3

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # gaussian sum

        not_total = sum(nums)
        n = len(nums)
        total = n*(n + 1)//2

        return total - not_total
        

        