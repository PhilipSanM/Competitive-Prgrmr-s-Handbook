# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 49. Group Anagrams -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: March - 26- 2024
# URL: https://leetcode.com/problems/first-missing-positive/description/
# ====================================================================

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1 - 4
        #i 0     1   2      3
        # [3,   4,  5,   1]
        #  |
        #                   if 1 <=  pointer <= len(nums)
        # pointer = 3 ->     nums[pointer - 1] = pointer

        
        # Fucking cycle sort
        # 1 <= solution <= len(nums)
        n = len(nums)
        for i in range(0, len(nums)):
            if nums[i] < 1:
                nums[i] = n + 1
            

        for i in range(0, len(nums)):
            if 1<= abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1]= abs(nums[abs(nums[i]) - 1])* (-1)


        for i in range(0, len(nums)):
            if nums[i] > 0:
                return i + 1

        
        return n + 1
