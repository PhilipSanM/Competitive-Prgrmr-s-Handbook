# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 57. Insert Interval -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 16- 2024
# URL: https://leetcode.com/problems/insert-interval/
# ====================================================================

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        index= 0

        result = []

        while index < len(intervals) and newInterval[0] > intervals[index][1]:
            result.append(intervals[index])
            index += 1


        while index < len(intervals) and newInterval[1] >= intervals[index][0]:
            newInterval[0] = min(newInterval[0],intervals[index][0])
            newInterval[1] = max(newInterval[1],intervals[index][1])
            index += 1

        result.append(newInterval)


        while index < len(intervals):
            result.append(intervals[index])
            index += 1


        return result
