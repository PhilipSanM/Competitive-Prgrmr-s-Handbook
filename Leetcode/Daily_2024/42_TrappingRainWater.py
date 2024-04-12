# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 42. Trapping Rain Water -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: April - 11- 2024
# URL: https://leetcode.com/problems/trapping-rain-water/description/
# ====================================================================

class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0, 1, 0, 2 , 1 , 0 , 1 , 3 ,2 , 1 , 2 , 1]
        #                                    L          R
        # width = 2
        # auxilir = 1 
        # Water = 5

        # Bro lmao with those two pointers:(

        # rule min(left_max, right_max) - height[i]


        L , R= 0, len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        water = 0
        index = 0

        while L < R:
            if left_max <= right_max:
                L += 1
                water += max(0, left_max - height[L])
                left_max = max(left_max,  height[L])
                
            else:
                R -= 1
                water += max(0, right_max - height[R])
                right_max = max(right_max, height[R])
                


        return water
        