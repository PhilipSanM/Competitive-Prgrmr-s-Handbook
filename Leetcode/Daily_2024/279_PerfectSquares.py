# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-279. Perfect Squares-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 08- 2024
# URL: https://leetcode.com/problems/perfect-squares/
# ====================================================================
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        aux = 1
        while aux ** 2 <= 10000:
            perfect_squares.append(aux**2)
            aux += 1
        

        dp = [n]*(n +1)
        dp[0] = 0
        for target in range(1, n + 1):
            for square in perfect_squares:
                aux = target - square

                if aux < 0:
                    break

                dp[target] = min(dp[target], 1 + dp[aux])



        return dp[n]