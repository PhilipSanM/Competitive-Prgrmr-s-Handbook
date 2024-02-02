# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=1291. Sequential Digits-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 2 - 2024
# URL: https://leetcode.com/problems/sequential-digits/
# ====================================================================

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        rule = "123456789"
        size = len(str(low))
        possible = True
        answer = []
        while possible:
            for i in range(0, len(rule) - size + 1):
                number = rule[i: i + size]
                if low <= int(number) <= high:
                    answer.append(int(number))
                # print(number)
                
                if int(number) > high:
                    possible = False

            size += 1
            if size >= len(rule) + 1:
                break




        return answer

