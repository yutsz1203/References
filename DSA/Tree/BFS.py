# 102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

from collections import deque

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