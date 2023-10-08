# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=- 2895. Minimum Processing Time =-=-=-=-=-=-=-=-=-=--=-=-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: October - 10 - 2023
# URL: https://leetcode.com/problems/minimum-processing-time/description/
# ====================================================================


# First Approach - Sorting
# Time Complexity : O(n)
# Space Complexity: O(n)


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks, processors, max_time = sorted(tasks), sorted(processorTime), 0 
        for pro_time in processors:
            max_time = max(max_time, pro_time + tasks[-1])
            tasks = tasks[:-4]

        return max_time