# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 1235. Maximum Profit in Job Scheduling -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: January - 23 - 2024
# URL: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
# ====================================================================

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        lengths =  [0, 0]

        def auxiliar(string, index, current_letters, cache):
            if index >= len(arr):
                return 0

            if string + arr[index] in cache:
                return cache[string + arr[index]]

            # adding solution
            cpy_letters = current_letters.copy()
            cpy_string = string[:]

            possible = ""
            possible_string = string[:]
            for char in arr[index]:
                if char not in current_letters:
                    possible_string += char
                    current_letters.add(char)
                else:
                    break

            if len(possible_string) == len(string) + len(arr[index]):
                string = possible_string[:]
            else:
                current_letters = cpy_letters.copy() 

            cache[string] = len(string)

            # print(string
            return max(cache[string],auxiliar(string, index + 1, current_letters, cache), auxiliar(cpy_string, index + 1, cpy_letters, cache) )

           
 


        return auxiliar("", 0, set(), {})
                
