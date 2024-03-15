class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(goal):
            if goal < 0: return 0

            current_sum = 0
            L = 0
            before = 0

            for R in range(len(nums)):
                current_sum += nums[R]

                while current_sum > goal:
                    current_sum -= nums[L]
                    L += 1

                before += R - L + 1

            return before



        return helper(goal) - helper(goal - 1)