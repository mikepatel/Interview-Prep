"""
https://leetcode.com/problems/subsets/
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = [[]]  # base case

        for n in nums:

            new_subsets = []
            for s in subsets:
                new_subsets.append(s + [n])

            subsets = subsets + new_subsets

        return subsets
