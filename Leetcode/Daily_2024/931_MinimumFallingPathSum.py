# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 931. Minimum Falling Path Sum -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 19 - 2024
# URL: https://leetcode.com/problems/minimum-falling-path-sum/description/
# ====================================================================


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def get_values(row, column, dp):
            curr = matrix[row][column]
            if column == 0:
                if len(matrix[row]) == 1:
                    return [curr + dp[column]]

                else:
                    
                    return [curr + dp[column + 1], curr + dp[column]]
            elif column == len(matrix[row]) - 1:
                # last position
                return [curr + dp[column - 1], curr + dp[column]]

            else:
                return [curr + dp[column - 1], curr + dp[column],curr + dp[column + 1] ]
            

        
        
        dp = matrix[-1] # [7, 8, 9]

        if len(matrix[0]) <= 1:
            return min(dp)

        for row in range(len(matrix) - 2, -1, -1):
            # one before the last positions:
            # print(dp)
            cpy = dp[:]
            for column in range(len(matrix[row])):
                possible_values = get_values(row, column, cpy)
                dp[column] = min(possible_values)
            

    
        return min(dp)

