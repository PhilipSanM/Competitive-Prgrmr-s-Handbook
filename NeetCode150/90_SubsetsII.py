# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 90. Subsets II  =-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: August - 11 - 2023
# URL: https://leetcode.com/problems/subsets-ii/description/
# ====================================================================

# Using Backtracking
# Two decisions:
#       1.- Adding the value
#       2.- Not adding the value + iterating when its different

# The solution on nums is 2^n
# Time complexity: O(n * 2^n) + O(nlogn)
# Space Complexity: O(n * 2^n)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        nums.sort()

        def makeDuplicates(index):
            if index >= len(nums):
                subsets.append(subset[:])
                return
            
            # Decision of adding value
            subset.append(nums[index])
            makeDuplicates(index + 1)
            # Not adding
            subset.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            makeDuplicates(index + 1)

        makeDuplicates(0)
        return subsets