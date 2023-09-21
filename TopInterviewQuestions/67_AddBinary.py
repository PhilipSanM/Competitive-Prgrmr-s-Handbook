# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-67. Add Binary =-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: February - 16- 2023
# URL: https://leetcode.com/problems/remove-element/
# ====================================================================


# First Approach - Using two pointers and a swap
# Time Complexity : O(n)
# Space Complexity: O(1)
# Runtime: 14 ms - Beats: 85.36% <> Memory: 13.33 MB - Beats: 68.85%


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j>= 0 :
                total += int(b[j])
                j -= 1

            result += str(total % 2)
            carry = total // 2

        return result[::-1]