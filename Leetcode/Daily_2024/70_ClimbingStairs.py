# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 70. Climbing Stairsa -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: January - 18- 2024
# URL: https://leetcode.com/problems/climbing-stairs
# ====================================================================

class Solution:
    def climbStairs(self, n: int) -> int:

        '''   _
            _|     3
          _|       2
        _|         1
       0
            [0]
            /  \
           [1]  [2]
           / \    / \
         [2] [3] [3] [4] -> 0
        / \
        [3] [4] -> 0

        3 ways for climbing so...

        '''

        # top-down-sol, with memoization
        goal = n
        def helper(position, cash):
            if position in cash:
                return cash[position]
            
            if position > goal:
                # There is no need to go further
                cash[position] = 0
                return cash[position]

            if position == goal:
                cash[position] = 1
                return cash[position]

            cash[position] = helper(position + 1, cash) + helper(position + 2, cash)
            
            return cash[position]


        return helper(0, {}) 