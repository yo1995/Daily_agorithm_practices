from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzag_traversal(r: TreeNode) -> List[List[int]]:

    if root:
        results = []
        s1 = []
        s1.append(root)
        is_odd = True
    else:
        return []

    while s1:
        l = []
        s2 = []
        while s1:
            top = s1.pop()
            if is_odd:
                if top.left:
                    s2.append(top.left)
                    pass
                if top.right:
                    s2.append(top.right)
                    pass
            else:
                if top.right:
                    s2.append(top.right)
                    pass
                if top.left:
                    s2.append(top.left)
                    pass
            l.append(top.val)
        results.append(l)
        s1 = s2
        is_odd = not is_odd

    return results
