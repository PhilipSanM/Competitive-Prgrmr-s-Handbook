# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 198. House Robber-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 22- 2024
# URL: https://leetcode.com/problems/house-robber/description/
# ====================================================================

#               -
# [1, 50, 1, 1, 10000] 0

# Two easy decisions will be:
    # 1.- rob ther house or skip
    # 2. - if you rob the house yo should skip next one
    # 3.- use DP

class Solution:
    def rob(self, nums: List[int]) -> int:


        def auxiliar(house, cash):
            if house >= len(nums):
                return 0 

            if house in cash:
                return cash[house]

            # Adding the solution

            cash[house] = max(nums[house] + auxiliar(house + 2, cash), auxiliar(house + 1, cash))

            return cash[house]

            # Skiping

        return auxiliar(0, {})