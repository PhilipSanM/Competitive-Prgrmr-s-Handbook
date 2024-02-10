# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 647. Palindromic Substrings -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 10- 2024
# URL: https://leetcode.com/problems/palindromic-substrings/
# ====================================================================

class Solution:
    def countSubstrings(self, s: str) -> int:
        L, R = 0,0
        # Odds
        count = 0

    
        for i in range(len(s)):
            L,R = i,i
            
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    count += 1
                else:
                    break
                R += 1
                L -= 1


        # Evens
        for i in range(len(s) - 1):
            L,R = i,i + 1
            
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    count += 1
                else:
                    break
                R += 1
                L -= 1




        
        return count
