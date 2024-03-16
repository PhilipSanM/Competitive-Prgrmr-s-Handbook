# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 253. Meeting Rooms II -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 15 - 2024
# URL: https://leetcode.com/problems/meeting-rooms-ii/
# ====================================================================

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 50
        # rooms = 2
        #  [[0,30], [5,10], [15,20], [40, 47], [42, 47], [43, 47]]
        #                                   -
        # [47, 47, 47]
        intervals = sorted(intervals)
        rooms = 0
        minheap = []

        for start, end in intervals:
            if minheap and minheap[0] <= start:
                heapq.heappop(minheap)

            heapq.heappush(minheap, end) 

    
        return len(minheap)
