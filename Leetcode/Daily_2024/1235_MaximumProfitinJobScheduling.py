# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1235. Maximum Profit in Job Scheduling -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Hard
# 
# Date: January - 6- 2024
# URL: https://leetcode.com/problems/maximum-profit-in-job-scheduling
# ====================================================================



class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # Add or not add the job
        '''
            (start, end, profit)
                        []
                       /   \ 
                    adding  NOT adding  - add index + 1
                    |
                check possibles and add
                continue with j
        '''

        intervals = zip(startTime, endTime, profit)
        intervals = sorted(intervals)

        cashe = {}


        def maximazing(index):
            if len(startTime) <= index:
                return 0

            if index in cashe:
                return cashe[index]


            # not adding the job
            resultant_profit = maximazing(index + 1)

            # add the job?
            # to do calculate j

            # adding a cash to make it more efficente O(n^2)
            # j = index + 1

             
            # while j < len(intervals):
            #     end = intervals[index][1]
            #     possible_start = intervals[j][0]

            #     if end <= possible_start:
            #         break

            #     j += 1

            # Binary search for 'j'
            j = bisect.bisect(intervals, (intervals[index][1], -1, -1))


            
            second_profit = maximazing(j)
            resultant_profit = max(resultant_profit, second_profit + intervals[index][2])

            cashe[index] = resultant_profit
            return resultant_profit

        return maximazing(0)



            
