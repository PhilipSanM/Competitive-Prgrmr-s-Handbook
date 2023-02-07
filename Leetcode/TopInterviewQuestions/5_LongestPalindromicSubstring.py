# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-5. Longest Palindromic Substring -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 07- 2023
# URL: https://leetcode.com/problems/longest-palindromic-substring/description/
# ====================================================================


# POWERED by Neetcode and remaked by me


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # s = "babad"
        #  First approach 
        # A while loop inside to check that palindromic
        #  s = "babad"
        #       _i___
        #       x  y
        # One index will go back and the other to the front

        max_substring = ""
        for i in range(len(s)):
            x,y = i,i
            substring = ''
            while x >= 0 and y <= len(s) - 1 and s[x] == s[y]:
                if x == y:
                    substring = s[x]
                else:
                    substring= s[x] + substring + s[y]
                if len(substring) > len(max_substring):
                    max_substring = substring
                x -= 1
                y += 1
            
            # EVEN
            x,y = i,i+1
            substring = ''
            while x >= 0 and y <= len(s) - 1 and s[x] == s[y]:
                substring= s[x] + substring + s[y]
                if len(substring) > len(max_substring):
                    max_substring = substring
                x -= 1
                y += 1
            

        
        return max_substring

# Time complexity = O(n^2)
# Space complexity = O(n^2)
