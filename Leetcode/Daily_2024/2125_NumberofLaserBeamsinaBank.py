# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 2125. Number of Laser Beams in a Bank -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 3- 2024
# URL: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
# ====================================================================


class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        total_lasers = 0
        lasers_A  = 0
       

        for cells in bank:
            lasers_B = cells.count("1")
            

                    


            if lasers_B > 0 :
                total_lasers += lasers_A*lasers_B
                lasers_A = lasers_B

        return total_lasers
                
