from collections import Counter
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        def traversal(node):
            c[node.val] += 1
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)

        if not root:
            return []
        c = Counter()
        traversal(root)
        mode, mode_freq = c.most_common()[0]
        result = [k for k in c if c[k] == mode_freq]
        return result

    def print_answer(self, ans):
        print(ans)

    def build_tree_inorder(self, vals):
        def build_tree_rec(node, i):
            if i < n:
                node = TreeNode(vals[i])
                node.left = build_tree_rec(node.left, 2*i+1)
                node.right = build_tree_rec(node.right, 2*i+2)
            return node

        n = len(vals)
        root = None
        root = build_tree_rec(root, 0)
        return root

    def print_tree(self, root):
        q = deque()
        q.append(root)
        level_order_vals = []
        while q:
            level_vals = []
            for i in range(len(q)):
                node = q.popleft()
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_order_vals.append(level_vals)
        print(level_order_vals)

    def test(self):
        vals = [1, 'null', 2, 2]
        root = self.build_tree_inorder(vals)
        self.print_tree(root)
        ans = self.findMode(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
