# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 347. Top K Frequent Elements -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 07 - 2023
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# ====================================================================


# First Approach - Using a hash-map
# Time Complexity : O(n)
# Space Complexity: O(n)



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        ans = []
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        dictionary_keys = list(dictionary.keys())
        dictionary_frequents = list(dictionary.values())

        

        for _ in range (k):
            
            max_frequent = max(dictionary_frequents)
            position_frequent = dictionary_frequents.index(max_frequent)
            key = dictionary_keys[position_frequent]
            
            position_key = dictionary_keys.index(key)

            ans.append(key)

            dictionary_keys.pop(position_key)
            dictionary_frequents.pop(position_frequent)

        return ans
