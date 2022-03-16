"""
https://leetcode.com/problems/merge-intervals/
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1. SORT over all pairs
        2. MERGE
        """
        # sort
        intervals = sorted(intervals, key=lambda x: x[0])

        output = []

        # TWO POINTERS
        left = intervals[0][0]
        right = intervals[0][1]

        # merge
        for i in range(1, len(intervals)):
            current_left = intervals[i][0]
            current_right = intervals[i][1]

            if current_left > right:
                # don't overlap
                output.append([left, right])
                left = current_left  # update left pointer
                right = current_right  # update right pointer

            else:  # do overlap
                if current_right > right:
                    right = current_right  # update right pointer

        # last pair
        output.append([left, right])

        return output
