# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 209. Minimum Size Subarray Sum  -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: July - 28 - 2023
# URL: https://leetcode.com/problems/minimum-size-subarray-sum/
# ====================================================================



# Sliding window
# Time Complexity : O(n)
# Space Complexity: O(1)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Using a sliding window appeoach
        #  [2,  3,   1,   2,  4,  3]  target = 7
        #            L        R
        #  curr = 7
        # length = 4   = R - L + 1   

        length = float("inf")
        L = 0
        curr = 0
        for R in range(len(nums)):
            curr += nums[R]
            while curr >= target:
                length = min(R - L + 1, length)
                curr -= nums[L]
                L += 1
            
        
        
        return length if length != float("inf") else 0