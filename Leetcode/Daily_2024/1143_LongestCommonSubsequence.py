# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-= 1143. Longest Common Subsequence-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 25 - 2024
# https://leetcode.com/problems/longest-common-subsequence/
# ====================================================================

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # two decision, taking the diagonall if there is the same letter, or the max betwenn two of the next subproblem
        #    a  c  e
        # -----------
        #  a|*
        #  b|     
        #  c|   *  
        #  d|      
        #  e|     *

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for row in range(len(text1) - 1, -1, -1):
            for column in range(len(text2) - 1, -1, -1):
                if text1[row] == text2[column]:

                    dp[row][column] = 1 + dp[row + 1][column + 1]
                else:
                    dp[row][column] = max(dp[row + 1][column], dp[row][column + 1])


        return dp[0][0]
