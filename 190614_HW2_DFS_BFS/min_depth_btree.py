from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def min_depth(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        md = 0
        q1 = deque()
        q1.append(root)

    while q1:
        q2 = deque()
        while q1:
            top = q1.popleft()
            if (not top.left) and (not top.right):
                return md
            if top.left:
                q2.append(top.left)
            if top.right:
                q2.append(top.right)
        md += 1
        q1 = q2
    # complete tree, just return the final result
    return md


def min_depth_recursive(self, root: TreeNode) -> int:
    if root is None:
        return 0
    # if root.left is None and root.right is None:
    #     return 1
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)
    if left != 0 and right != 0:
        return min(left, right) + 1
    else:
        return left + right + 1


def min_depth_stack(root: TreeNode) -> int:
    # since nothing to do with order, stack is better in space complexity
    if not root:
        return 0

    depth = 1
    stack = [root]

    while stack:
        next_level = []
        for node in stack:
            if not node.left and not node.right:
                return depth
            else:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        stack = next_level
        depth += 1
