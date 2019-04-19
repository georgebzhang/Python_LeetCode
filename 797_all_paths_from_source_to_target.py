class Solution(object):
    # don't convert graph to dict, since nodes are indices, and array lookup at index is fast
    def allPathsSourceTarget(self, graph):
        def rec(node):
            if node == N-1:
                return [[N-1]]
            result = []
            for neighbor in graph[node]:
                for path in rec(neighbor):
                    result.append([node] + path)
            return result

        N = len(graph)
        return rec(0)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        graph = [[1, 2], [3], [3], []]
        ans = self.allPathsSourceTarget(graph)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
