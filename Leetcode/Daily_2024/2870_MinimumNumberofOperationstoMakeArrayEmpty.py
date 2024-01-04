# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 2870. Minimum Number of Operations to Make Array Empty-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 4- 2024
# URL: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty
# ====================================================================


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2 ->1
        # 3 = 1
        # 4  -> 2
        # 5 -> 2
        # 6 -> 2
        # 7 -> 3 + 4 -> 3
        # 8 -> 6 + 2 -> 3
        # 9 -> 3
        # 10 -> 4 
        # 11, 12
        # 13,14,15  5
        # 16,17,18  6
        # 19,20,21  7
        # 19/3 = 6 - 1
        # 20/3 = 6 - 1
        # 21 = 7


        integers = {}

        for num in nums:
            integers[num] = integers.get(num, 0) + 1
        
        moves = 0
        for num in integers:
            if integers[num] == 1:
                return -1

            moves += integers[num] // 3
            if integers[num] % 3:
                moves += 1

        return moves

