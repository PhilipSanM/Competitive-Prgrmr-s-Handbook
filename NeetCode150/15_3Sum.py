# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 15. 3Sum -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: May - 24 - 2023
# URL: https://leetcode.com/problems/3sum/
# ====================================================================


# First Approach - 
# Time Complexity : O(n^2)
# Space Complexity: O(n)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[j] + nums[k] > 0 - nums[i]:
                        k -= 1
                    elif nums[j] + nums[k] < 0 - nums[i]:
                        j += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k]])
                        k -= 1
                        j += 1
                        while nums[j] == nums[j - 1] and j < k:
                            j += 1 
        
        return ans


