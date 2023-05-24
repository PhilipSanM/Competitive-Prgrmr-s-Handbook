# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 11. Container With Most Water -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: May - 24 - 2023
# URL: https://leetcode.com/problems/container-with-most-water/description/
# ====================================================================


# First Approach - 
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_contain = 0
        l, r = 0 , len(height) - 1
        base = len(height) - 1
        while l < r:
            
            h = min(height[l], height[r])
            actual_contain = h*base
            max_contain = max(max_contain, actual_contain)
            
            while height[l] <= h and l < r:
                l += 1
                base -= 1
        
            while height[r] <= h and l < r:
                r -= 1
                base -= 1
            



        return max_contain