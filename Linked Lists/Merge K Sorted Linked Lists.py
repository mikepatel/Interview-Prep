"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        1. iterate through the nodes of each linked list
        2. collect each node's value --> list
        3. sort the list
        4. create a new linked list from the list of all the sorted values
        """

        temp = []

        # iterate through the nodes of each linked list and
        # collect each node's value
        for li in lists:  # li --> linked list
            while li:
                temp.append(li.val)
                li = li.next

        # sort values
        temp = sorted(temp)

        # create a new linked list
        dummy = ListNode()
        current = dummy

        for value in temp:
            current.next = ListNode(val=value)
            current = current.next

        return dummy.next
