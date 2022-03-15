"""
https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        MULTIPLE POINTERS
        1. sort list
        2. Get 1st value
        3. Use left and right pointers to find values 2 and 3
        """
        output = []

        # edge case
        if len(nums) < 3:
            return []

        # sort
        nums = sorted(nums)

        integers = {}

        for i in range(len(nums)):
            a = nums[i]

            if a in integers:
                continue

            else:  # 'a' not in integers
                integers[a] = True

                # 2 pointers
                j = i + 1  # left-side pointer
                k = len(nums) - 1  # right-side pointer

                while j < k:
                    b = nums[j]
                    c = nums[k]

                    if a + b + c == 0:
                        output.append([a, b, c])
                        j = j + 1  # shift left-side pointer

                        # eliminate duplicates by sliding left-hand side pointer upwards
                        while (j < k) and (nums[j] == nums[j - 1]):
                            j = j + 1

                    elif a + b + c > 0:  # shift right-side pointer
                        k = k - 1

                    else:  # a + b + c < 0, shift left-side pointer
                        j = j + 1

        return output
