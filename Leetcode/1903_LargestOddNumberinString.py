# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1903. Largest Odd Number in String-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: December - 12- 2023
# URL: https://leetcode.com/problems/largest-odd-number-in-string/description/
# ====================================================================

# First Approach - Using a set
# Time Complexity : O(n)
# Space Complexity: O(n)
# Runtime: 14 ms - Beats: 79.38% <> Memory: 12.95 MB - Beats: 98.41%


class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        end = len(num) - 1

        longest = ""

        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                # odd
                return num[:i + 1]

        return ""