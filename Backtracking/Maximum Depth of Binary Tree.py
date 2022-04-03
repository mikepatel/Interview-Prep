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
            # pre-order traversal

            # stopping condition
            if node is None:
                return depth

            else:
                return max(
                    dfs(node=node.left, depth=depth + 1),  # left subtree
                    dfs(node=node.right, depth=depth + 1)  # right subtree
                )

        # driver code
        max_depth = dfs(node=root, depth=0)
        return max_depth
