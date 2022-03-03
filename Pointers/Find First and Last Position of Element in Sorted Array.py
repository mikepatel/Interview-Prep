"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # BRUTE FORCE
        if target not in nums:
            return [-1, -1]

        else:  # 'target' is in 'nums'
            mapper = {}  # key=value, value=list of indices

            for i in range(len(nums)):
                n = nums[i]

                if n in mapper:  # seen before
                    mapper[n].append(i)

                else:  # not seen before
                    mapper[n] = [i]

            #
            indices = mapper[target]
            first = indices[0]
            last = indices[-1]
            return [first, last]

        # LEFT and RIGHT POINTERS
