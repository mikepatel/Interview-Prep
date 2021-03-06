"""
https://leetcode.com/problems/jump-game/
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # POINTER
        # MOVE BACKWARDS: target --> 0, instead of 0 --> target
        target_index = len(nums) - 1

        # move backwards
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target_index:  # can I make the jump from here?
                target_index = i  # reset --> move further back

        if target_index == 0:  # reached the beginning
            return True

        else:
            return False
