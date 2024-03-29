# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 340. Longest Substring with At Most K Distinct Characters -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 28 - 2024
# URL: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# ====================================================================

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        letters = defaultdict(int)
        
        longest = 0
        L = 0
        for R in range(len(s)):
            letters[s[R]] += 1
            

            while len(letters) > k:
                letters[s[L]] -= 1
                if letters[s[L]] == 0:
                    letters.pop(s[L])

                L += 1

            
            longest = max(longest, R- L + 1)


        return longest