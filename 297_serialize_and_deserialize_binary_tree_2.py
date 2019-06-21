from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        levels_vals = []
        q = deque([root])
        while q:
            level_vals = []
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    level_vals.append('null')
                    continue
                level_vals.append(node.val)
                q.append(node.left)
                q.append(node.right)

            if not all(val == 'null' for val in level_vals):
                levels_vals.extend(level_vals)

        return levels_vals

    def deserialize(self, data):
        def deserialize_rec(node, ind):
            if ind < len(data):
                node = TreeNode(data[ind])
                node.left = deserialize_rec(node.left, 2*ind + 1)
                node.right = deserialize_rec(node.right, 2*ind + 2)

            return node

        return deserialize_rec(None, 0)


class Solution(object):
    def print_answer(self, ans):
        print(ans)

    def build_tree(self, vals):
        def build_tree_rec(node, ind):
            if ind < len(vals):
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
        vals = [1, 2, 3, 'null', 'null', 4, 5]
        root = self.build_tree(vals)
        self.print_tree(root)
        codec = Codec()
        self.print_tree(codec.deserialize(codec.serialize(root)))


if __name__ == '__main__':
    s = Solution()
    s.test()
