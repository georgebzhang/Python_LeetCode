from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalancedDepth(self, node, result):
        if not result[0]:
            return 0
        left_depth = 0 if not node.left else self.isBalancedDepth(node.left, result)
        right_depth = 0 if not node.right else self.isBalancedDepth(node.right, result)
        if abs(left_depth-right_depth) > 1:
            result[0] = False
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root):
        if not root:
            return True
        result = [True]
        self.isBalancedDepth(root, result)
        return result[0]

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
