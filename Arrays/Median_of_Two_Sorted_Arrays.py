"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2  # merge
        arr = sorted(arr)  # sort

        arr_length = len(arr)

        if arr_length == 0:  # no elements
            return 0
        elif arr_length == 1:  # 1 element
            return arr[0]
        else:  # at least 2 elements
            if arr_length % 2 == 0:  # even
                median_index = int(arr_length / 2)
                total = arr[median_index - 1] + arr[median_index]
                return float(total / 2)
            else:  # odd
                median_index = int(arr_length / 2)
                return arr[median_index]
