# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-2971. Find Polygon With the Largest Perimeter -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 14- 2024
# URL: https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description
# ====================================================================\

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # [1,12,1,2]
        #       -
        # [1, 1, 12]   -> [1, 1, 2, 3, 5, 12, 50]
        #                                   -
        #                  P = 7    polygon = [1, 1, 2, 3, 5] 
        #                    possible?  yes


    

        
        perimeter = -1

        while len(nums) >= 3:
            max_side = max(nums)
            total = sum(nums)
            
            if total > max_side*2 :
                # possible
                return total
            
            nums.remove(max_side)
            

            
            

        return perimeter