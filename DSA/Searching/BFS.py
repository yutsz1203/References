# 102. Binary Tree Level Order Traversal
from collections import deque

from Tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            level_size = len(q)
            curr_level = []

            for _ in range(level_size):
                node = q.popleft()
                curr_level.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

            res.append(curr_level)

        return res
