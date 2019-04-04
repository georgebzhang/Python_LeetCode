from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def equal(self, node_s, node_t):
        curr_equal = node_s.val == node_t.val
        if node_s.left and node_t.left:
            left_equal = self.equal(node_s.left, node_t.left)
        else:
            left_equal = node_s.left is node_t.left
        if node_s.right and node_t.right:
            right_equal = self.equal(node_s.right, node_t.right)
        else:
            right_equal = node_s.right is node_t.right
        return curr_equal and left_equal and right_equal

    def isSubtree(self, s, t):
        if not t:
            return True  # empty tree (t) is always subtree of another tree (s)
        if not s:
            return not t  # empty tree (t) is only subtree of empty tree (s)
        if self.equal(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

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
        s_vals = [3, 4, 5, 1, 2]
        t_vals = [4, 1, 2]
        s = self.build_tree_inorder(s_vals)
        t = self.build_tree_inorder(t_vals)
        self.print_tree(s)
        self.print_tree(t)
        ans = self.isSubtree(s, t)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
