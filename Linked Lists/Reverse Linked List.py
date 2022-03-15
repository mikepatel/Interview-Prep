"""
https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Modifying the same Linked List --> while head:
        """
        """
        # initialize
        prev = None
        current = head

        while current:
            temp = current.next  # placeholder, step 3
            current.next = prev  # want previous node to now come after current node, step 2
            prev = current  # want current node to become previous node, step 1

            current = temp  # iterate

        return prev
        """

        # initialize
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
