# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 739. Daily Temperatures-=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 31- 2024
# URL: https://leetcode.com/problems/daily-temperatures/
# ====================================================================

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # using monotonic stack
        stack = [] # (temperature, index)
        answer = [0 for _ in range(len(temperatures))]

        for index in range(len(temperatures)):
            while stack and temperatures[index] > stack[-1][0]:
                # poping
                temperature_data = stack.pop()
                days = index - temperature_data[1]

                answer[temperature_data[1]] = days


            
            # adding
            stack.append((temperatures[index], index))

        
        return answer