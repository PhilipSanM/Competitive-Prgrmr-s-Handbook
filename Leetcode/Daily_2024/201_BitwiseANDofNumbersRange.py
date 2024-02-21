# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 201. Bitwise AND of Numbers Range -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 20- 2024
# URL: https://leetcode.com/problems/bitwise-and-of-numbers-range/
# ====================================================================

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #  8 4 2 1
        #  0 1 0 1
        #  0 1 1 0
        # -------
        #  0 1 0 0

        shift = 0
        


        while left > 0 and right > 0:
            if left == right:
                return left << shift

            shift += 1
            left = left >> 1
            right = right >> 1

        return 0
