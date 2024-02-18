# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-2402. Meeting Rooms III-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: February - 18 - 2024
# URL: https://leetcode.com/problems/meeting-rooms-iii/
# ====================================================================

#         [2, 2]
#   occupied = [0, 1]        [[0,10],[1,5],[2,7],[3,4]]
#  notoccuied = []                                 m
#       duration = 1    [10, 0, 11]  -    
#   minqueue = [[10, 0, 0], [10, 1, 5]] 
# [end, room, start]


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        total_rooms = [0]* n
        available = [i for i in range(n -1, -1, -1) ]
        meetings.sort()
        
        minheap = []
        heapq.heapify(available)

        

        for meeting in meetings:
            
            start = meeting[0]
            end = meeting[1]

            while minheap and minheap[0][0] <= start:
                data = heapq.heappop(minheap)
                room = data[1]
                heapq.heappush(available, room)
            
            if not available:
                # logic of men heap
                finished_meeting = heapq.heappop(minheap)
                duration = end - start

                start = finished_meeting[0]
                room = finished_meeting[1]
                end = start + duration

                heapq.heappush(available, room)
                

            room = heapq.heappop(available)
            data = [end, room, start]
            total_rooms[room] += 1
            heapq.heappush(minheap, data)


        
        max_room = max(total_rooms)
        return total_rooms.index(max_room)