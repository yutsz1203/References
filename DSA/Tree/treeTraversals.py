# Tree traversals uses DFS with stacks in iterative approaches

from Tree import TreeNode

# Inorder traversal
# Left -> Root -> Right
# Produce list of node vals inorder


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
    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if cur and node.val <= cur.val:
            return False
        cur = node
        node = node.right

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


# Postorder Traversal
# Left -> Right -> Root
# Produce list of node vals postorder


# Iterative with one stack
# Reference: https://leetcode.com/problems/binary-tree-postorder-traversal/solutions/5669641/binary-tree-postorder-traversal/
def postorderTraversalIterativeOneStack(root: TreeNode) -> list[int]:
    res = []

    if root is None:
        return res

    stack = []
    prev = None

    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack[-1]

            if (
                root.right is None or root.right == prev
            ):  # root.right == prev when all nodes of right subtree have been processed, at original root for example
                res.append(root.val)
                stack.pop()
                prev = root
                root = None
            else:
                root = root.right

    return res


# Iterative with two stacks (one stack of node (TreeNode), another stack of visited (bool))
# Reference: https://youtu.be/QhszUQhGGlA?si=oSIYK2svCJjMESqp
def postorderTraversalIterativeTwoStacks(root: TreeNode) -> list[int]:
    stack = [root]
    visit = [False]
    res = []

    while stack:
        cur, visited = stack.pop(), visit.pop()
        if cur:
            if visited:
                res.append(cur.val)
            else:
                stack.append(cur)
                visit.append(True)
                stack.append(cur.right)
                visit.append(False)
                stack.append(cur.left)
                visit.append(False)
                cur = cur.left

    return res


# Reversing pre order traversal
def postorderReversePreorder(root: TreeNode) -> list[int]:
    res = []
    stack = []
    cur = root

    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.right
        else:
            cur = stack.pop()
            cur = cur.left
        res.reverse()

    return res


# Recursive
def postorderTraversalRecursive(root: TreeNode) -> list[int]:
    res = []

    def postorder(root):
        if root is None:
            return
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)

    postorder(root)
    return res
