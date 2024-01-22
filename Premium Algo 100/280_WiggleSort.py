# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 280. Wiggle Sort -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 22 - 2023
# URL: https://leetcode.com/problems/wiggle-sort/
# ====================================================================


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # less, bigger, less, bigger, less, biger
        # [3, 3, 4]
        #           -
        # [3,3,2,  ]
        #      |
        # index = 1
        # [7, 1]

        state = "bigger"

        for index in range(1, len(nums)):
            if state == "bigger" and nums[index] < nums[index -1]:
                # print(nums[index])
                auxiliar = index - 1
                while auxiliar >= 0  and nums[index] < nums[auxiliar]:
                    if nums[index] <= nums[auxiliar]:
                        # print(index, auxiliar)
                        # swap
                        nums[index], nums[auxiliar] = nums[auxiliar], nums[index]
                        break
                    
                    auxiliar -= 1
            
            
            if state == 'less' and nums[index] > nums[index -1]:
                # print(nums[index])
                auxiliar = index - 1
                while auxiliar >= 0  and nums[index] > nums[auxiliar]:
                    if nums[index] >= nums[auxiliar]:
                        # swap
                        nums[index], nums[auxiliar] = nums[auxiliar], nums[index]
                        break

                    auxiliar -= 1

            state = 'bigger' if state == 'less' else 'less'
            # print(nums)

