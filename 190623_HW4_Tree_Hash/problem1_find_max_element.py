
def find_max(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    m = [0]
    helper(root, m)
    return m[0]


def helper(n, m):
    if n.val > m[0]:
        m[0] = n.val
    if n.left:
        helper(n.left, m)
    if n.right:
        helper(n.right, m)
