from collections import deque, defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        def bfs(node):
            q = deque([(node, 0)])
            while q:
                node, column = q.popleft()
                if not node:
                    continue
                map[column].append(node.val)
                q.append((node.left, column-1))
                q.append((node.right, column+1))

        if not root:
            return []

        map = defaultdict(list)  # {column: [vals]}
        bfs(root)

        result = []
        columns = sorted(map)
        for c in columns:
            result.append(map[c])

        return result

    def print_answer(self, ans):
        print(ans)

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
        vals = [3, 9, 8, 4, 0, 1, 7, 'null', 'null', 'null', 2, 5]
        root = self.build_tree(vals)
        self.print_tree(root)
        ans = self.verticalOrder(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
