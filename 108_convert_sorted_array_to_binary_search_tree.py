from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        def sortedArrayToBSTHelper(node, ind_left, ind_right):
            if ind_left == ind_right:
                return TreeNode(nums[ind_left])
            if ind_right-ind_left == 1:
                node = TreeNode(nums[ind_left])
                node.right = TreeNode(nums[ind_right])
                return node

            ind_mid = (ind_left+ind_right)//2
            node = TreeNode(nums[ind_mid])
            node.left = sortedArrayToBSTHelper(node.left, ind_left, ind_mid-1)
            node.right = sortedArrayToBSTHelper(node.right, ind_mid+1, ind_right)
            return node

        if not nums:
            return []
        n = len(nums)
        root = None
        root = sortedArrayToBSTHelper(root, 0, n-1)
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

    def print_answer(self, ans):
        self.print_tree(ans)

    def test(self):
        vals = [-10, -3, 0, 5, 9]
        ans = self.sortedArrayToBST(vals)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
