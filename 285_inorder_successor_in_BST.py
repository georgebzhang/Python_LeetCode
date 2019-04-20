from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        def traverse(node):
            if not node:
                return

            traverse(node.left)
            if self.successor:
                return
            if node.val > p.val:
                self.successor = node
            traverse(node.right)

        self.successor = None
        traverse(root)
        return self.successor

    def print_answer(self, ans):
        print(ans.val)

    def build_tree(self, vals):
        def build_tree_rec(node, ind):
            if ind < len(vals):
                if vals[ind] != 'null':
                    node = TreeNode(vals[ind])
                    node.left = build_tree_rec(node.left, 2 * ind + 1)
                    node.right = build_tree_rec(node.right, 2 * ind + 2)
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
        vals = [5, 3, 6, 2, 4, 'null', 'null', 1]
        root = self.build_tree(vals)
        p = TreeNode(1)
        self.print_tree(root)
        ans = self.inorderSuccessor(root, p)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
