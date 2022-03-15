"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        BRUTE FORCE --> TWO POINTERS
        """

        # Approach 1
        # BRUTE FORCE
        """
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
        """

        # Approach 2
        # LEFT and RIGHT POINTERS

        # edge cases
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]

            else:
                return [-1, -1]

        # TWO pointers
        left = 0
        right = len(nums) - 1

        while left < right:
            # squeeze window from the left-side
            if nums[left] < target:
                left = left + 1  # increment left-side pointer

            else:  # nums[left] >= target
                # squeeze window from the right-side
                if nums[left] > target:
                    return [-1, -1]

                else:  # nums[left] == target

                    while nums[right] > target:
                        right = right - 1  # decrement right-side pointer

                    # nums[right] <= target
                    if nums[right] == target:
                        return [left, right]

        # did not find target in window
        # --> possible that left=right and nums[left] == nums[right] == target
        if nums[left] == target:
            return [left, right]

        else:
            return [-1, -1]

