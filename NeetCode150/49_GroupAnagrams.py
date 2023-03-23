class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # First approach usign brute force:
        # iterating trhough strs and then iteration in every letter of a word
        # then checking for every array in our array answer 
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a - z
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return res.values()
                

        # O(m * n)

                    
