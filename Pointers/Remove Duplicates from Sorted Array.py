"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # REQ: in-place modification

        # approach 1: python functions
        # nums[:] = sorted(list(set(nums)))

        # approach 2: pointer --> while loop
        i = 0
        while i < len(nums) - 1:  # cannot use for-loop because modifying the length of nums --> index out of range
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)

            else:
                i += 1

        return len(nums)

