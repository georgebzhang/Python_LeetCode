from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def max_depth(self, node):
        if not node:
            return 0
        return max(self.max_depth(node.left), self.max_depth(node.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_height = self.max_depth(root.left)
        right_height = self.max_depth(root.right)
        curr_balanced = abs(left_height-right_height) <= 1
        return curr_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)

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
        vals = [3, 9, 20, 'null', 'null', 15, 7]
        root = self.build_tree_inorder(vals)
        self.print_tree(root)
        ans = self.isBalanced(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
