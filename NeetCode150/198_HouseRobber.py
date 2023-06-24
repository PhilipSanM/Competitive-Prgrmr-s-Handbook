
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 167. Two Sum II - Input Array Is Sorted -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: june - 23 - 2023
# URL: https://leetcode.com/problems/house-robber/
# ====================================================================


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#       [1,  2,  3,  1]
#       [1 , 2,   4,   4>3.. 4]

#       [4,  2, 11, 1, 2, 100]
#       [17, 115]

        dp = [0,0]

        for num in nums:
            temp = max(dp[1], num + dp[0])
            dp[0] = dp[1]
            dp[1] = temp

        return dp[1]