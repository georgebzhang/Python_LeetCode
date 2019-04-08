from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []

        map = {}  # {child node: parent node}
        leaves = []
        stack = [root]  # stack for DFS
        while stack:
            n = stack.pop()
            if not n.left and not n.right:  # leaf
                leaves.append(n)
            if n.left:
                stack.append(n.left)
                map[n.left] = n
            if n.right:
                stack.append(n.right)
                map[n.right] = n

        paths = []
        for n in leaves:
            path = [str(n.val)]
            while True:
                try:
                    parent = map[n]
                    path.append(str(parent.val))
                    n = parent
                except:
                    break
            path.reverse()
            paths.append(path)

        result = []
        for p in paths:
            str_path = ''
            for val in p:
                str_path += val + '->'
            result.append(str_path[:-2])
        return result

    def print_answer(self, ans):
        print(ans)

    def build_tree_inorder(self, vals):
        def build_tree_rec(node, i):
            if i < n:
                if vals[i] != 'null':
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
                if node.val == 'null':
                    continue
                if node.left:
                    q.append(node.left)
                else:
                    q.append(TreeNode('null'))
                if node.right:
                    q.append(node.right)
                else:
                    q.append(TreeNode('null'))
            level_order_vals.append(level_vals)
        print(level_order_vals)

    def test(self):
        vals = [1, 2, 3, 'null', 5]
        root = self.build_tree_inorder(vals)
        self.print_tree(root)
        ans = self.binaryTreePaths(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
