# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 191. Number of 1 Bits -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: june - 23 - 2023
# URL: https://leetcode.com/problems/number-of-1-bits/description/
# ====================================================================

# First Approach - bit manipulation
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_bits = 0
        while n > 0:
            if n & 1:
                num_bits += 1
            n= n >> 1

        return num_bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_bits = 0
        while n > 0:

            num_bits += 1
            n= n & (n-1)

        return num_bits


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")

