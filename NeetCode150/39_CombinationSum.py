# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 39. Combination Sum-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: June - 04 - 2023
# URL: https://leetcode.com/problems/combination-sum/description/
# ====================================================================

# Using backtracking
# O(2^n)

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        combination = []

        def makeAllCombinations(index, total):
            if total == target:
                combinations.append(combination[:])
                return
            if total > target or index >= len(candidates):
                return
            
            # Adding the same value
            combination.append(candidates[index])
            total += candidates[index]
            makeAllCombinations(index, total)

            # Not adding it
            combination.pop()
            total -= candidates[index]
            makeAllCombinations(index + 1, total)



        makeAllCombinations(0, 0)
        
        return combinations

