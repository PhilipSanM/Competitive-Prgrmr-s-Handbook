# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 27. Remove Element-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: july - 03- 2023
# URL: https://leetcode.com/problems/roman-to-integer/description/
# ====================================================================


# First Approach - Hashmap
# Time Complexity : O(n)
# Space Complexity: O(1)


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M":1000
        }
        curr = 1
        res = 0
        for i in range(len(s) - 1, -1, -1):
            value = romans[s[i]]
            if value >= curr:
                curr = value
                res += value
            else:
                res -= value
        return res