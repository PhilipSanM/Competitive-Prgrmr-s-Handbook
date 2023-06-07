# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 141. Linked List Cycle -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: June - 06 - 2023
# URL: https://leetcode.com/problems/linked-list-cycle/
# ====================================================================


# First Approach - Using a set
# Time Complexity : O(n)
# Space Complexity: O(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        allnodes = {}
        while head:
            if head in allnodes:
                return True
            else:
                allnodes[head] = 0

            head = head.next
        return False