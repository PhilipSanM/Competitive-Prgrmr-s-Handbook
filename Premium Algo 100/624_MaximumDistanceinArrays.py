# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 3624. Maximum Distance in Arrays -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 22 - 2023
# URL: https://leetcode.com/problems/maximum-distance-in-arrays
# ====================================================================


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        actual_min = arrays[0][0]
        actual_max = arrays[0][-1]

        max_distance = 0

        for index in range(1, len(arrays)):
            array = arrays[index]
            max_distance = max(max_distance, abs(actual_min - array[-1]), abs(actual_max - array[0]))
            actual_min = min(actual_min, array[0])
            actual_max = max(actual_max, array[-1])



        return max_distance
