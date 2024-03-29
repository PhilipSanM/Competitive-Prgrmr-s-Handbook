# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=2962. Count Subarrays Where Max Element Appears at Least K Times=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 28- 2024
# URL: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# ====================================================================


class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # [1,   3,  2,  3, 3]
        #  ___R
        # count = 0
        # indexes = [2, 4, 5] 
        #             A
        # ans = 8
        # 
        # 
        # 
        maximum = max(nums)
        indexes = []
        auxiliar = 0
        answer = 0
        count = 0
        
        for R in range(len(nums)):
            if nums[R] == maximum:
                indexes.append(R + 1)
                count += 1

            if nums[R] == maximum and count > k:
                auxiliar += 1

            if count >= k:
                answer += indexes[auxiliar]


        return answer
        