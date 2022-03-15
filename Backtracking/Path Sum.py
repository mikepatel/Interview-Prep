"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Since searching a tree, use DFS

        # dfs helper
        def dfs(node, total):
            if node is None:
                return False

            total = total + node.val

            if node.left is None and node.right is None:
                # leaf node
                if total == targetSum:
                    return True

            else:
                return dfs(node=node.left, total=total) or dfs(node=node.right, total=total)

        # driver code
        return dfs(node=root, total=0)
