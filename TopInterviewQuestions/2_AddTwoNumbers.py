# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=- Add Two Numbers =-=-=-=-=-=-=-==-=-=-=-=-=-=
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Medium
# 
# Date: February - 02 - 2023
# URL: https://leetcode.com/problems/add-two-numbers/
# ====================================================================


#  My Solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        point_l1 = l1
        point_l2 = l2
        carry = 0
        result = ListNode()
        point_result = result
        
        while point_l1 != None and point_l2 != None:
            z = (point_l1.val + point_l2.val + carry) % 10
            point_result.val = z
            if point_l1.val + point_l2.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            if point_l1.next != None or point_l2.next != None:
                point_result.next = ListNode()
            
            if point_l1.next == None and point_l2.next == None and carry==1:
                point_result.next = ListNode()
            point_result = point_result.next
            point_l1 = point_l1.next
            point_l2 = point_l2.next
            if point_l1 == None and point_l2 != None:
                bigguer_list = point_l2
            elif point_l2 == None and point_l1 != None:
                bigguer_list = point_l1
            else:
                bigguer_list = None

        
        while bigguer_list != None:
            z = (bigguer_list.val + carry) % 10
            point_result.val = z

            if bigguer_list.val + carry >= 10:
                carry = 1
            else:
                carry = 0

            if bigguer_list.next != None :
                point_result.next = ListNode()
            elif bigguer_list.next != None or carry ==1:
                point_result.next = ListNode()

            bigguer_list = bigguer_list.next
            point_result = point_result.next


        if carry == 1:
            point_result.val = carry
        
        return result

           # Time complexity: O(N)
# Space Complexity: O(N) 
        


    
















