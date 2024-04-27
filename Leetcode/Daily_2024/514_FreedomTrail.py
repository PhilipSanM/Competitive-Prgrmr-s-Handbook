# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 514. Freedom Trail -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: April - 27- 2024
# URL: https://leetcode.com/problems/freedom-trail/
# ====================================================================

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        distances = defaultdict(list)

        for index, letter in enumerate(ring):
            distances[letter].append(index)


        cache = {}

        def helper(ring_index, key_index):
            if  key_index >= len(key):
                return 0

            if (ring_index, key_index) in cache:
                return cache[(ring_index, key_index)]

            distance = float("inf")

            
            for position in distances[key[key_index]]:
                movement = min(
                    abs(ring_index - position), # right
                    len(ring) - abs(ring_index - position) # left
                )

                distance = min(
                    distance,
                    movement + 1 + helper(position, key_index + 1)
                )

                
            cache[(ring_index, key_index)] = distance


            return distance



        return helper(0, 0)

