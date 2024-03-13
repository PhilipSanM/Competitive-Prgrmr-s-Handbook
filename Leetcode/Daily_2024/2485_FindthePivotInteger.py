# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-2485. Find the Pivot Integer-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: March - 12 - 2024
# URL: https://leetcode.com/problems/find-the-pivot-integer/description/
# ====================================================================


class Solution:
    def pivotInteger(self, n: int) -> int:
        gauss_number = n*(n + 1) // 2
        addition = 0
        for number in range(n + 1):
            addition += number
            
            if addition == gauss_number:
                return number

            gauss_number -= number

            

        return -1