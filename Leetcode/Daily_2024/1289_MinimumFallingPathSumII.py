# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-1289. Minimum Falling Path Sum II-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: April - 25 - 2024
# URL: https://leetcode.com/problems/minimum-falling-path-sum-ii/
# ====================================================================

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 1:
            return min(grid[0])


        last_row = grid[-1]
        
        for row in range(len(grid) - 2, -1, -1):
            
            for column in range(len(grid[0])):

                grid[row][column] = grid[row][column] + min(last_row[:column] + last_row[column + 1:])

            last_row = grid[row]


        return min(last_row)
