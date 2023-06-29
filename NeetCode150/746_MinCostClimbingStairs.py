# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 746. Min Cost Climbing Stairs -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: June - 29 - 2023
# URL: https://leetcode.com/problems/min-cost-climbing-stairs/description/
# ====================================================================

# First Approach - 1-DP
# Time Complexity : O(n)
# Space Complexity: O(1)


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # [1   ,100   ,1   ,1   ,1    ,100   ,1   ,1   ,100    ,1]
        # [0, 0 ]
        if len(cost) < 2:
            return cost[0]
        if len(cost) < 3:
            return min(cost[0],cost[1])

        dp = [cost[0], cost[1]]
        for i in range(2, len(cost) - 1):
            temp = min(dp[0] + cost[i], dp[1] + cost[i])
            dp[0] = dp[1]
            dp[1] = temp

        return min(dp[1], dp[0] + cost[-1])
    
    # Post: https://leetcode.com/problems/min-cost-climbing-stairs/solutions/3697890/8-a-1-dp-buttom-up-solution-using-python/