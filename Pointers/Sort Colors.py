"""
https://leetcode.com/problems/sort-colors/
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # step 1: keep track of number of 0's, 1's, 2's
        freqs = {
            0: 0,
            1: 0,
            2: 0
        }

        for n in nums:
            freqs[n] += 1

        # step 2: modify in-place according to counts
        nums_index = 0
        for i in range(3):
            while freqs[i]:
                nums[nums_index] = i
                freqs[i] -= 1
                nums_index += 1

        # Using a for-loop instead of a while-loop
        index = 0
        for value in range(3):  # 0, 1, 2
            for _ in range(freqs[value]):
                nums[index] = value  # what needs to go in
                index += 1  # where it needs to go in

        # 3rd solution: 1 for-loop
        for i in range(len(nums)):
            if freqs[0] > 0:
                nums[i] = 0
                freqs[0] -= 1

            elif freqs[1] > 0:
                nums[i] = 1
                freqs[1] -= 1

            else:  # freqs[2] > 0
                nums[i] = 2
                freqs[2] -= 1
