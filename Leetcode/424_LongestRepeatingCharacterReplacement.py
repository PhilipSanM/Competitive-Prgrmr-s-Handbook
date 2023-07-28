# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 392. Is Subsequence -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: July - 28 - 2023
# URL: https://leetcode.com/problems/longest-repeating-character-replacement/
# ====================================================================



# Sliding window
# Time Complexity : O(26n)  = O(n)
# Space Complexity: O(26) = O(1)




class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # s = "A    C   B     F    G    B     A"  k = 2
        #      L,R
        # length = 0    mostfreq =     condition: length - mostFrequency =< k
        # cash = {   A:  frequ}
        length = 0
        L = 0
        letters = {}
        for R in range(len(s)):
            letters[s[R]] = 1 + letters.get(s[R], 0)
            
            while (R - L + 1) - max(letters.values()) > k:
                letters[s[L]] -= 1
                L += 1


            length = max(length, R - L + 1)

        
        return length

        
