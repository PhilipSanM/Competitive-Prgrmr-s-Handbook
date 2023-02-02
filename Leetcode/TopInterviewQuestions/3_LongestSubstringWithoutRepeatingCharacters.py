# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-3. Longest Substring Without Repeating Characters =-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 02 - 2023
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# ====================================================================


#  My Solution

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # USING Split in PY

        # "pswfwkew"
        # sub= 'w'
        # best = 'pswf'
        # "asqwertyui"
        sub = ''
        best = ''
        for letter in s:
            if letter in sub:
                if len(best) < len(sub):
                    best = sub
                sub = sub[sub.index(letter) + 1 :] + letter
            else:
                sub += letter
                
        if len(sub) > len(best):
            best = sub
        return len(best)

# Time complexity: O(N)
# Space Complexity: O(N)