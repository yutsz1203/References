# Tree traversals uses DFS with stacks in iterative approaches

from Tree import TreeNode

# Inorder traversal
# Left -> Root -> Right
# List of node vals inorder


# Reference: https://www.youtube.com/watch?v=g_S5WuasWUE
# Iterative
def inorderTraversalIterative(root: TreeNode):
    res = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right

    return res


# Iterative application
# Reference: https://www.youtube.com/watch?v=gGsEVFP0aQo
# Leetcode 98. Validate Binaray Search Tree
def isValidBST(root: TreeNode) -> bool:
    if root is None:
        return True

    stack = []
    cur = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if cur and root.val <= cur.val:
            return False
        cur = root
        root = root.right

    return True


# Recursive
def inorderTraversalRecursive(root: TreeNode):
    res = []

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res
