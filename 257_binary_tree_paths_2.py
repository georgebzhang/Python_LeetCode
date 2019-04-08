from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        def traversal(node):
            if not node:
                return
            path.append(str(node.val))
            traversal(node.left)
            if not node.left and not node.right:
                paths.append(path.copy())
            traversal(node.right)
            path.pop()

        paths = []
        path = []
        traversal(root)
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
