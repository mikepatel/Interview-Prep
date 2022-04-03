"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # backtrack
        def dfs(node, depth):
            # stopping condition
            if node is None:
                return depth

            else:
                # pre-order traversal
                return max(
                    dfs(node=node.left, depth=depth + 1),
                    dfs(node=node.right, depth=depth + 1)
                )

        # driver code
        max_depth = dfs(node=root, depth=0)
        return max_depth
