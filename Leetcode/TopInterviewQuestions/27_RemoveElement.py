# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 27. Remove Element-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: February - 16- 2023
# URL: https://leetcode.com/problems/remove-element/
# ====================================================================


# First Approach - Using two pointers and a swap
# Time Complexity : O(n)
# Space Complexity: O(1)
# Runtime: 15 ms - Beats: 90.42% <> Memory: 13.4 MB - Beats: 43.91%
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # nums = [0,1,3,0,4,0,4,2], val = 2
        #                   i   j
        index = 0

        # Using a two pointers approach
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index


# Second approach  - Using a Two pointes again
# Time Complexity : O(n)
# Space Complexity: O(1)
# Runtime: 26 ms - Beats: 31.33% <> Memory: 13.4 MB - Beats: 43.91%

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # nums = [0,1,3,0,4,0,4,2], val = 2
        #                   i   j
        index = 0

        # Using a two pointers approach
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index


# POST: https://leetcode.com/problems/remove-element/solutions/3194493/python-3-two-solution-solutions-using-two-pointers-runtime-15-ms-beats-90-42/
