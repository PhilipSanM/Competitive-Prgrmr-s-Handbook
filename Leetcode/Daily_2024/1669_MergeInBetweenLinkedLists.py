# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=1669. Merge In Between Linked Lists -=-=-=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: March - 19 - 2024
# URL: https://leetcode.com/problems/merge-in-between-linked-lists/
# ====================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        pointer = list1
        counter = 0
        while pointer:
            if counter + 1 == a:
                node_a = pointer
            
            if counter - 1 == b:
                node_b = pointer
                break

            pointer = pointer.next
            counter += 1

        node_a.next = list2
        

        pointer = node_a
        while pointer.next:
            pointer = pointer.next

        pointer.next = node_b

        return head

            