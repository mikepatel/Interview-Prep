"""
https://leetcode.com/problems/3sum-closest/
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # sort
        nums.sort()

        # initialize
        total = float("inf")
        diff = float("inf")

        for i in range(len(nums)):
            a = nums[i]

            # initialize inner pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                b = nums[left]
                c = nums[right]

                current_total = a + b + c
                current_diff = abs(current_total - target)

                if current_diff < diff:
                    diff = current_diff
                    total = current_total

                if current_total < target:
                    left += 1

                else:
                    right -= 1

        return total
