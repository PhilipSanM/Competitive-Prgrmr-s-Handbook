# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 125. Valid Palindrome -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: May - 22 - 2023
# URL: https://leetcode.com/problems/valid-palindrome/
# ====================================================================


# First Approach - iterating in all the array
# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = ""
        for letter in s:
            if letter.isalnum():
                d += letter

        return d[::-1].lower() == d.lower()
        