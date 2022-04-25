"""
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # approach 1
        nums1[m: m + n] = nums2
        nums1.sort()

        # approach 2
        # pop all empties in nums1
        # append all elements in nums2 to nums1
        # sort

#         # edge cases
#         if m == 0 and n == 0:
#             nums1 = []

#         elif m == 0:
#             nums1 = nums2

#         elif n == 0:
#             nums1 = nums1

#         else:
#             count = n
#             while count > 0:
#                 nums1.pop()
#                 count -= 1

#             for i in range(n):
#                 nums1.append(nums2[i])

#             nums1.sort()
