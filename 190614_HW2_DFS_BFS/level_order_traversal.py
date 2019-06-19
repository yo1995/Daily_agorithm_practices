from collections import deque


def level_order_traversal(r):
    q = deque()
    q.append(r)
    while q:
        top = q.popleft()
        print(top.val)
        if top.left:
            q.append(top.left)
            pass
        if top.right:
            q.append(top.right)
            pass
