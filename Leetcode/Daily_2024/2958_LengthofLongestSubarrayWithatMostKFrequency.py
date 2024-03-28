# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-2958. Length of Longest Subarray With at Most K Frequency-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 28- 2024
# URL: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# ====================================================================

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        L = 0
        longest = 0
        cashe = defaultdict(int)
        
        for R in range(len(nums)):
            cashe[nums[R]] += 1
            while cashe[nums[R]] > k:
                cashe[nums[L]] -= 1
                L += 1

            longest = max(longest, R - L + 1)


        return longest