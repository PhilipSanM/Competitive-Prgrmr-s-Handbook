# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-2225. Find Players With Zero or One Losses -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 15- 2024
# URL: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
# ====================================================================


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = set()
        unvictus = set()
        one_match_lost = set()

        for winer, loser in matches:

            if winer not in losers and winer not in one_match_lost:
                unvictus.add(winer)


            if loser in unvictus:
                unvictus.remove(loser)





            if loser in one_match_lost and loser not in losers:
                losers.add(loser)
                # print(loser)
                one_match_lost.remove(loser)

            if loser not in losers:
                one_match_lost.add(loser)

                
        return[sorted(list(unvictus)),sorted(list(one_match_lost)) ]