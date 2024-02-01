# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 2966. Divide Array Into Arrays With Max Difference -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 31- 2024
# URL: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
# ====================================================================\

class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        answer = []
        nums.sort()
        

        for i in range(0, len(nums), 3):
            if i + 2 < len(nums) and nums[i + 2] - nums[i] <= k:
                answer.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []


        return answer

