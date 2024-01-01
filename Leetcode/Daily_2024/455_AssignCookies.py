# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 455. Assign Cookies -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: January - 1- 2023
# URL: https://leetcode.com/problems/assign-cookies/description/
# ====================================================================

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i,j =0,0
        happy_kids = 0
        g,s = sorted(g), sorted(s)

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                happy_kids += 1
                j += 1
                i += 1

            else:
                j += 1


        return happy_kids