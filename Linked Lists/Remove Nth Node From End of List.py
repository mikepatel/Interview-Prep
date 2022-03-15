"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of linked list
        num_nodes = 0

        temp = head
        while temp:
            temp = temp.next
            num_nodes += 1

        #
        # remove Nth from the last node
        target = num_nodes - n
        i = 0
        prev = ListNode(val=None, next=head)
        dummy = head

        while head:
            if target == 0:  # edge case: remove first node in LinkedList
                return head.next

            elif i == target:  # remove Nth node in LinkedList
                prev.next = head.next
                head = head.next

            else:  # keep iterating through LinkedList
                prev = head
                head = head.next

            i += 1

        return dummy
