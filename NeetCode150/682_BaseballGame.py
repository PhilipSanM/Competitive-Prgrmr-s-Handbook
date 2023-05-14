# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 347. Top K Frequent Elements -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: May - 14 - 2023
# URL: https://leetcode.com/problems/baseball-game/description/
# ====================================================================


# First Approach - 
# Time Complexity : O(n)
# Space Complexity: O(n)


class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        answer = []
        for operation in operations:
            if operation == 'C':
                answer.pop()
            elif operation == 'D':
                number = answer[-1]
                answer.append(number * 2)
            elif operation == '+':
                number1 = answer[-1]
                number2 = answer[-2]
                answer.append(number1 + number2)
            
            else:
                answer.append(int(operation))
            
        return sum(answer)