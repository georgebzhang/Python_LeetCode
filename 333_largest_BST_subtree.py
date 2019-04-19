from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        def BST_rec(node, lower=None, upper=None):
            if not node:
                return True

            curr = None
            if lower is not None and upper is not None:
                curr = node.val > lower and node.val < upper
            elif lower is not None:
                curr = node.val > lower
            elif upper is not None:
                curr = node.val < upper
            else:
                curr = True

            left = BST_rec(node.left, lower, node.val)
            right = BST_rec(node.right, node.val, upper)
            return curr and left and right

        def size_rec(node):
            if not node:
                return 0

            return size_rec(node.left) + size_rec(node.right) + 1

        def largest_BST_rec(node):
            if not node:
                return

            if BST_rec(node):
                BST_sizes.append(size_rec(node))

            largest_BST_rec(node.left)
            largest_BST_rec(node.right)

        if not root:
            return 0
        BST_sizes = []
        largest_BST_rec(root)
        return max(BST_sizes)

    def print_answer(self, ans):
        print(ans)

    def build_tree(self, vals):
        def build_tree_rec(node, ind):
            if ind < len(vals):
                if vals[ind] != 'null':
                    node = TreeNode(vals[ind])
                    node.left = build_tree_rec(node.left, 2*ind + 1)
                    node.right = build_tree_rec(node.right, 2*ind + 2)
            return node

        root = build_tree_rec(None, 0)
        return root

    def print_tree(self, root):
        q = deque()
        q.append(root)
        result = []
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    temp.append('null')
                    continue
                temp.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if not all(val == 'null' for val in temp):
                # result.append(temp)  # for result = [[1], [2, 3], ['null', 'null', 4, 5]]
                result.extend(temp)  # for result = [1, 2, 3, 'null', 'null', 4, 5]
        print(result)

    def test(self):
        vals = [10, 5, 15, 1, 8, 'null', 7]
        root = self.build_tree(vals)
        self.print_tree(root)
        ans = self.largestBSTSubtree(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
