# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 155. Min Stack -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: May - 21 - 2023
# URL: https://leetcode.com/problems/longest-consecutive-sequence/description/
# ====================================================================


# First Approach - Using a set
# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        len = 0
        for num in nums:
            if num - 1 not in nums:
                size = 1
                while num + size in nums:
                    size += 1
                len = max(len,size)
        return len

