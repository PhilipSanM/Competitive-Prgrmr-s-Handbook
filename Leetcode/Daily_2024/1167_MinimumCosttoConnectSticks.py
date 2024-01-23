# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-= 938. Range Sum of BST -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 23 - 2024
# URL: https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# ====================================================================

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0

        
        heapq.heapify(sticks)
        price = 0

        while len(sticks) > 1:
            first_stick = heapq.heappop(sticks)

            second_stick = heapq.heappop(sticks)

            new_stick = first_stick + second_stick

            price += new_stick

            heapq.heappush(sticks, new_stick)

        return price
