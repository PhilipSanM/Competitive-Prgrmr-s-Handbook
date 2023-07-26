# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=- 347. Top K Frequent Elements -=-=-=-=-=-=-=-=-=-=-==
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Easy
# 
# Date: May - 14 - 2023
# URL: https://leetcode.com/problems/merge-two-sorted-lists/description/
# ====================================================================


# First Approach - 
# Time Complexity : O(n)
# Space Complexity: O(n)



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Taking the two list and comparing values
        #Adding all the elements and if it points tu null
        # just add all the elements of the list that still have elements
        # Also you dont need to create another list
        answer_list = ListNode()
        answer_list.next = list1
        tail = answer_list


        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
            else:
                tail.next = list1
                list1 = list1.next
                tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return answer_list.next
