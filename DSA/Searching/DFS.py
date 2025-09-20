# DFS traverses at a selected node and explores as deep as possible down one path before backtracking, using a stack.
# Leetcode 104. Maximum Depth of Binary Tree
from Tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
        return res
