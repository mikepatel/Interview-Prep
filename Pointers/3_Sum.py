"""
https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        if len(nums) < 3:
            return []

        # sort
        nums = sorted(nums)

        integers = {}

        for i in range(len(nums)):
            a = nums[i]

            if a in integers:
                continue

            else:
                integers[a] = True

                # 2 pointers
                j = i + 1
                k = len(nums) - 1

                while j < k:
                    b = nums[j]
                    c = nums[k]

                    if a + b + c == 0:
                        output.append([a, b, c])
                        j = j + 1

                        # eliminate duplicates by sliding left-hand side pointer upwards
                        while (j < k) and (nums[j] == nums[j - 1]):
                            j = j + 1

                    elif a + b + c > 0:
                        k = k - 1

                    else:  # a + b + c < 0
                        j = j + 1

        return output
