from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBSTHelper(node, lower_limit, upper_limit):
            # is not None is needed, since limits can be zero
            if lower_limit is not None and node.val <= lower_limit:
                return False
            if upper_limit is not None and node.val >= upper_limit:
                return False
            valid_left = isValidBSTHelper(node.left, lower_limit, node.val) if node.left else True
            if valid_left:
                return isValidBSTHelper(node.right, node.val, upper_limit) if node.right else True
            else:
                return False

        if not root:
            return True
        return isValidBSTHelper(root, None, None)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        ans = self.isValidBST(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
