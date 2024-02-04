# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-= 1043. Partition Array for Maximum Sum -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 3 - 2024
# URL: https://leetcode.com/problems/partition-array-for-maximum-sum/description/
# ====================================================================

class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # [15  15 20  20]
        #
        # [ 0 15 7  20]
        #    _
        # k = 3
        # max = 1 

        def dfs(index, cache):
            if index >= len(arr):
                return 0

            curr_max = 0
            res = 0

            if index in cache:
                return cache[index]

            for j in range(index, min(len(arr), index + k)):
                window_size = j - index + 1
                curr_max = max(curr_max, arr[j])

                res = max(res, dfs(j + 1, cache) + curr_max * window_size)
                cache[index] = res


            return res


        return dfs(0, {})



                
