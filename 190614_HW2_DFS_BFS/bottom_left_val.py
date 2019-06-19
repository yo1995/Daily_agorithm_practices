from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# https://leetcode.com/problems/find-bottom-left-tree-value/submissions/
def findBottomLeftValue(root: TreeNode) -> int:
    if not root:
        return -1
    else:
        first_value = -1
        q1 = deque()
        q1.append(root)
        pass

    while q1:
        q2 = deque()
        l = []
        while q1:
            top = q1.popleft()
            if top.left:
                q2.append(top.left)
                pass
            if top.right:
                q2.append(top.right)
            l.append(top.val)
        first_value = l[0]
        q1 = q2

    return first_value


def f2(root: TreeNode) -> int:

    if not root:
        return -1
    else:
        first_value = -1
        is_first = False
        q1 = deque()
        q1.append(root)
        pass

    while q1:
        is_first = True
        q2 = deque()
        while q1:
            top = q1.popleft()
            if is_first:
                first_value = top.val
                is_first = False
            if not top.left and not top.right:
                continue
            if top.left:
                q2.append(top.left)
                pass
            if top.right:
                q2.append(top.right)
        q1 = q2

    return first_value
