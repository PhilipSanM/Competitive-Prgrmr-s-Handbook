# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 78. Subsets  -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: June - 04 - 2023
# URL: https://leetcode.com/problems/subsets/description/
# ====================================================================

# Using Backtracking
# Two decisions:
#       1.- Adding the value
#       2.- Not adding the value

# The solution on nums is 2^n
# Time complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        subset = []
        def makeAllSubsets(index):
            if index >= len(nums):
                subsets.append(subset[:])
                return
        
            # Adding solution:
            subset.append(nums[index])
            makeAllSubsets(index + 1)

            # Not adding the solution
            subset.pop()
            makeAllSubsets(index + 1)

        makeAllSubsets(0)
        return subsets

