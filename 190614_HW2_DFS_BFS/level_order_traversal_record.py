from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_traversal(r: TreeNode) -> List[List[int]]:
    results = []
    q1 = deque()
    if r:
        q1.append(r)
    else:
        return results

    while q1:
        level_result = []
        q2 = deque()
        while q1:
            top = q1.popleft()
            if top.left:
                q2.append(top.left)
                pass
            if top.right:
                q2.append(top.right)
                pass
            level_result.append(top.val)
        results.append(level_result)
        q1 = q2
    # if need to reverse
    # results.reverse()
    return results


def level_order_traversal_delimiter(root: TreeNode) -> List[List[int]]:
    results = []
    q = deque()
    if root:
        q.append(root)
        q.append(None)
    else:
        return results

    level_result = []
    while q:
        top = q.popleft()
        if not top:  # a null delimiter
            results.append(level_result)
            if q:
                q.append(None)
                level_result = []
        else:
            if top.left:
                q.append(top.left)
                pass
            if top.right:
                q.append(top.right)
                pass
            level_result.append(top.val)
    results.reverse()
    return results


def recursive(r: TreeNode) -> List[List[int]]:
    results = []
    if not root:
        return results
    helper(root, 0, results)
    return results


def helper(t: TreeNode, level: int, res: List[List[int]]):
    if not t:
        return
    if level == len(res):
        res.insert(0, [])
        pass
    l = res[len(res) - 1 - level]
    if t.left:
        helper(t.left, level + 1, res)
    if t.right:
        helper(t.right, level + 1, res)
    l.append(t.val)
    return













