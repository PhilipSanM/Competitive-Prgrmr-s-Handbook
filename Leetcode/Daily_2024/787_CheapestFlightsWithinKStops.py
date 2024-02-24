# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 787. Cheapest Flights Within K Stops -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 23 - 2024
# URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# ====================================================================

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # OMG BELLMANS-FORD
        prices = [float("inf")] * n
        prices[src] = 0


        for _ in range(k + 1):
            auxiliar = prices[:]

            for source, destiny, price in flights:
                if prices[source] == float("inf"):
                    continue

                if prices[source] + price < auxiliar[destiny]:
                    auxiliar[destiny] = prices[source] + price


            prices = auxiliar




        return prices[dst] if prices[dst] != float("inf") else -1