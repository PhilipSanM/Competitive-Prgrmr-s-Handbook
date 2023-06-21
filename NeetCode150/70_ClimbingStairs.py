# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 70. Climbing Stairs  =-=-=-=--=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: June - 20 - 2023
# URL: https://leetcode.com/problems/climbing-stairs/
# ====================================================================


# 1 - DP
class Solution:
    def climbStairs(self, n):
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
    

# Memoization
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
            2
          /  \
         2    2  --> 2
        / \
        1  1
        

        
        4
        1 + 1 + 1 + 1
        1 + 2 + 1
        2 + 2
        1 + 1 + 2
        2 + 1 + 1 
        5  -> 3   2
        """
        # Base case
    
        return self.memoClimb(n , {}) 

    
    def memoClimb(self, n , cache):
        if n <= 2:
            return n 
        if n in cache:
            return cache[n]

        cache[n] = self.memoClimb(n - 2, cache) + self.memoClimb(n - 1, cache) 
        return cache[n]

        