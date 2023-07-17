# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 392. Is Subsequence -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: July - 17 - 2023
# URL: https://leetcode.com/problems/is-subsequence/description/
# ====================================================================




# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        for letter in t:
            if l < len(s) and letter == s[l]:
                l += 1

        return l == len(s) 