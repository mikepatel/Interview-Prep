"""
https://leetcode.com/problems/permutations/
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # backtrack
        def backtrack(visited):

            # stopping condition
            if len(visited) == len(nums):
                permutations.append(visited.copy())  # add new list since 'visited' will be modified
                return

            # continue searching
            else:
                for n in nums:
                    if n not in visited:
                        # apply value
                        visited.append(n)

                        # backtrack
                        backtrack(visited)

                        # remove value
                        visited.pop(-1)

        # driver code
        permutations = []
        backtrack(visited=[])

        return permutations
