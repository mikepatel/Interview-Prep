"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()  # dummy head
        output = dummy

        while list1 and list2:  # while both are non-empty
            if list1.val <= list2.val:
                output.next = list1  # set next node

                output = output.next  # advance
                list1 = list1.next  # advance

            else:
                output.next = list2  # set next node
                
                output = output.next  # advance
                list2 = list2.next  # advance

        # at least one is empty
        if list1:
            output.next = list1

        else:
            output.next = list2

        return dummy.next
