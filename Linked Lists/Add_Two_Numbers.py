"""
https://leetcode.com/problems/add-two-numbers/
"""


################################################################################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


################################################################################
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize
        dummy_head = ListNode()  # dummy head
        current = dummy_head  # initialize current node to dummy head
        carry = 0

        # traverse linked lists
        while l1 or l2 or carry:
            # check if reached end of linked list
            if l1:
                a = l1.val
            else:
                a = 0

            if l2:
                b = l2.val
            else:
                b = 0

            #
            total = carry + a + b
            carry = int(total / 10)
            total = total % 10

            # go to next node
            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None

            current.next = ListNode(val=total)
            current = current.next

        return dummy_head.next  # don't return dummy head
