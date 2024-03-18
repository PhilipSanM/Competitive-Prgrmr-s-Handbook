# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=452. Minimum Number of Arrows to Burst Balloons -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 18- 2024
# URL: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# ====================================================================

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points)

        arrows = 0

        #    [1,  9]  
        #     [2, 5]

        #    [3,  7]
        #     [4  5]
        #      [6,  9] 
        # max(6)   min (5)
        #  6 > 5  ballon used
        # 5 <= 5
            #  [6, 9]
        #                     |
        # [1,2],[3,4],[5,6],[7,8]
        # start      end
        # max = 7  min = 8
        # arros = 3

        max_aux = points[0][0]
        min_aux = points[0][1]
        for start, end in points:
            max_aux = max(max_aux, start)


            if max_aux > min_aux:
                arrows += 1
                min_aux = end

            min_aux = min(min_aux, end)


        
        arrows += 1

        return arrows


        