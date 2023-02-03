# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-4. Median of Two Sorted Arrays  -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 03- 2023
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
# ====================================================================


#  My Solution
        # First Approach : Brute Force -> T(N) = O(n) + O(nlogn) => O(nlog)
                                            # S(N) = O(n)
        # nums1 = [1,2], nums2 = [3,4]
        # merge and sort [1,2,3,4]     (2+3) / 2 = 2.5 
        # 
        #                  -----
        # len(merge) = 5
        # max_index = len -1 = 4
        # mid 5//2 = 2
        # return index of mid if len an even

        # Odd: len = 4
        # max_index = 3
        # mid = 4//2 = 2 
        # Sub_mid = mid - 1 = 1   
        # return index sub_mid + mid / 2

        # Second approach
        # Test case
        # [2,5,8] [1,9]
        #      i     j
        # binary seach -> 9 -1 = 8 
        # new_array = [1,5,8,9,...]
        # T(N) = O(log(m + n)) O(1) = > O(log(m+n))
        # S(N) = O(n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_array = []
        new_array = nums1 + nums2
        new_array.sort()
        len_array = len(new_array)
        mid = len_array // 2

        if len_array % 2 == 0:
            sub_mid =  mid - 1 
            return (new_array[sub_mid] + new_array[mid] ) / 2.0
        else:
            return new_array[mid]



# Time complexity: O(nlogn)
# Space Complexity: O(N)



# This is a try Using binary Seach ;)
class Solution(object):
    def binary_search(slef,nums,value_to_find):
        another_value = value_to_find
        while True:
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) / 2
                guess = nums[mid]
                if guess == another_value:
                    return mid
                elif guess > another_value:
                    high = mid - 1
                else:
                    low = mid + 1
            another_value += -1

            


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def binary_search(nums,value_to_find):
            another_value = value_to_find
            while True:
                low = 0
                high = len(nums) - 1
                while low <= high:
                    mid = (low + high) / 2
                    guess = nums[mid]
                    if guess == another_value:
                        return mid
                    elif guess > another_value:
                        high = mid - 1
                    else:
                        low = mid + 1
                another_value += -1
        new_array = []
        len_array = 0
        i = 0
        j = 0
        while len_array != len(nums1) + len(nums2) and i != len(nums1) and  j != len(nums2):
            if nums1 == None or nums2 ==None:
                if nums1 == None:
                    new_array = nums2
                else:
                    new_array = nums1
            elif nums1[i] < nums2[j]:
                value_to_find = nums2[j] - 1
                index = binary_search(nums1,value_to_find)

                aux = nums1[i:index]
                new_array += aux 
                new_array += [nums1[index]]
                i = index
            elif nums1[i] > nums2[j]:
                value_to_find = nums2[i] - 1
                index = binary_search(nums2,value_to_find)
                aux = nums2[j:index]
                new_array += aux 
                new_array += [nums2[index]]
                j = index
            elif nums1[i] == nums2[j]:
                aux = []
                aux += [nums1[i]]
                aux += [nums2[j]]
                new_array += aux
            i += 1
            j += 1
            len_array = len(new_array)
        print(new_array)

        if i == len(nums1) or j == len(nums2):
            if i == len(nums1):
                aux = nums2[j-1:]
                print(aux)
                new_array += aux 
            else:
                aux = nums1[i:]
                new_array += aux

        print(new_array)
        len_array = len(new_array)
        mid = len_array // 2
        # odd number
        if len_array % 2 == 0:

            sub_mid =  mid - 1 
            print(sub_mid)
            print(mid)
            return (new_array[sub_mid] + new_array[mid] ) / 2.0
        else:
            return new_array[mid]

