# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 576. Out of Boundary Paths -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 26- 2023
# URL: https://leetcode.com/problems/out-of-boundary-paths/
# ====================================================================

class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
     
        
        def dfs(current_move, row, column, cache):
            if min(row, column) < 0 or row >= m or column >= n:
                return 1

            
            if current_move >= maxMove:
                return 0

            if (row, column, current_move) in cache:
                return cache[(row, column, current_move)]

            cache[(row, column, current_move)] = dfs(current_move + 1, row + 1, column, cache) + dfs(current_move + 1, row - 1, column, cache) + dfs(current_move + 1, row, column + 1, cache) + dfs(current_move + 1, row, column - 1, cache)

            return cache[(row, column, current_move)] % MOD



        return dfs(0, startRow, startColumn, {})
            
