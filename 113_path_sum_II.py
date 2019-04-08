from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, target):
        def traversal(node):
            if not node:
                return
            stack.append(node.val)
            traversal(node.left)
            if not node.left and not node.right:
                if sum(stack) == target:
                    paths.append(stack.copy())
            traversal(node.right)
            stack.pop()

        stack = []
        paths = []
        traversal(root)
        return paths

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
        vals = [5, 4, 8, 11, 'null', 13, 4, 7, 2, 'null', 'null', 'null', 'null', 5, 1]
        root = self.build_tree_inorder(vals)
        target = 22
        self.print_tree(root)
        ans = self.pathSum(root, target)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
