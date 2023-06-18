# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 153. Find Minimum in Rotated Sorted Array -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: May - 18 - 2023
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# ====================================================================


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [2,          1]
        #  l,mid       r                
        # l = 0
        # r = 1
        #mid = 0
        # curr = 4

        l, r = 0, len(nums) - 1
        curr_min = nums[0]
        while l <= r:
            mid = (l + r) // 2
            curr_min = min(curr_min, nums[mid], nums[l], nums[r])
            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid -1
 

        return curr_min
                