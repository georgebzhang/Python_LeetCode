# https://www.youtube.com/watch?v=4fiDs7CCxkc
# https://leetcode.com/problems/largest-bst-subtree/discuss/78895/Short-Python-solution
from collections import deque
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        # Returns:
        # 1. bool: is subtree at node BST?
        # 2. size of max BST in subtree at node
        # 3. lower limit and 4. upper limit of BST at node (does not matter if subtree at node is not BST)
        def traversal(node):
            if not node:
                return True, 0, sys.maxsize, -sys.maxsize
            BST_l, size_BST_l, lower_l, upper_l = traversal(node.left)
            BST_r, size_BST_r, lower_r, upper_r = traversal(node.right)
            if BST_l and BST_r and upper_l < node.val < lower_r:
                return True, size_BST_l+size_BST_r+1, min(lower_l, node.val), max(upper_r, node.val)
            else:
                return False, max(size_BST_l, size_BST_r), 0, 0  # lower limit and upper limit don't matter

        BST, size, lower, upper = traversal(root)
        return size

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
