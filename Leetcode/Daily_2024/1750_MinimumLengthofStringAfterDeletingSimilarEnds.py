# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=1750. Minimum Length of String After Deleting Similar Ends -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 04- 2024
# URL: https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
# ====================================================================


class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        L, R = 0, len(s) - 1
        size = len(s)
        prev = ""
        while L < R:
            
            if s[L] == s[R]:
                prev = s[L]
                L += 1
                R -= 1
                
                size -= 2

            elif s[L] == prev:
                size -= 1
                L += 1

            elif s[R] == prev:
                R -= 1
                size -= 1

            else:
                break

        if L == R and s[L] ==prev:
            L += 1
        
        return R-L+1