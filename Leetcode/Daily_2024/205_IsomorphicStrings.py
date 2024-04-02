# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 205. Isomorphic Strings -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: April - 01- 2024
# URL: https://leetcode.com/problems/isomorphic-strings/
# ====================================================================

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        L = 0
        cashe = {}
        mapped = {}
        for R in range(0, len(t)):
            if s[L] in cashe and cashe[s[L]] != t[R]:
                return False

            if t[R] in mapped and mapped[t[R]] != s[L]:
                return False

            cashe[s[L]] = t[R]
            mapped[t[R]] = s[L]
            L += 1


        return True
