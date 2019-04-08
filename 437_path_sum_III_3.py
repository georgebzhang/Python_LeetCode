from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, target):
        def num_ways(node, remain):
            if not node:
                return 0
            found = 0 if node.val != remain else 1
            return found + num_ways(node.left, remain-node.val) + num_ways(node.right, remain-node.val)

        def traversal(node):
            if not node:
                return 0
            return num_ways(node, target) + traversal(node.left) + traversal(node.right)

        return traversal(root)

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
        vals = [10, 5, -3, 3, 2, 'null', 11, 3, -2, 'null', 1]
        root = self.build_tree_inorder(vals)
        target = 8
        self.print_tree(root)
        ans = self.pathSum(root, target)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
