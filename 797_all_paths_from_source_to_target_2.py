from collections import deque


class Solution(object):
    # don't convert graph to dict, since nodes are indices, and array lookup at index is fast
    def allPathsSourceTarget(self, graph):
        N = len(graph)

        paths = []
        path = [0]
        q = deque([path])
        while q:
            path = q.popleft()
            last = path[-1]
            if last == N-1:
                paths.append(path)  # don't need path[:], since copies are made below
            for node in graph[last]:
                q.append(path[:] + [node])

        return paths

    def print_ans(self, ans):
        print(ans)

    def test(self):
        graph = [[1, 2], [3], [3], []]
        ans = self.allPathsSourceTarget(graph)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
