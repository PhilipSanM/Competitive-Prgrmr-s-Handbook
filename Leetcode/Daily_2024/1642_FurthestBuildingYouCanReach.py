# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=1642. Furthest Building You Can Reach -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 17 - 2024
# URL: https://leetcode.com/problems/furthest-building-you-can-reach/description/
# ====================================================================

# 100 bricks and 1 ladder
# if it's possible use bricks if not a lader
#                         
#                    ---    
#           -----     101
#            1       
#      ---     if possible bricks?
#        ladder first?
# 
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxheap = []

        for i in range(len(heights) - 1):
            difference = heights[i + 1] - heights[i]

            if difference <= 0 :
                continue

            bricks -= difference

            heapq.heappush(maxheap, -difference)

            if bricks < 0:
                if ladders == 0:
                    return i
                # use a ladder and return bricks
                ladders -= 1

                resultant_bricks = -heapq.heappop(maxheap)
                bricks += resultant_bricks




        return len(heights) - 1