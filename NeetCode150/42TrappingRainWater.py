# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 42. Trapping Rain Water-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: May - 25 - 2023
# URL: https://leetcode.com/problems/trapping-rain-water/description/
# ====================================================================


# First Approach - Two pointers
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        water = 0
        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        while l < r:        
            if height[l] <= height[r]:
                l += 1
                if left_max < height[l]:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
            else:
                r -= 1
                if right_max < height[r]:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
        return water



        