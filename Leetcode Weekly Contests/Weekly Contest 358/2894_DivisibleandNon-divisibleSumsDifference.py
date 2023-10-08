# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=- 2894. Divisible and Non-divisible Sums Difference -=-=-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: October - 10 - 2023
# URL: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference
# ====================================================================


# First Approach - iterating over the numbers
# Time Complexity : O(n)
# Space Complexity: O(1)


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        additions = 0
        sustractions = 0
        
        for i in range(1, n + 1):
            if i % m == 0:
                sustractions += i
            else:
                additions += i
                
        return additions - sustractions