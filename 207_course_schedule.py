from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        def dfs(v):
            if v in visited:
                return
            if v in visiting:
                self.result = False
                print('Cycle!')
                return
                # raise Exception('Cycle!')
            visiting.add(v)
            for n in g[v]:  # for neighbor of vertex
                dfs(n)

            visiting.remove(v)
            visited.add(v)
            order.append(v)

        self.result = True
        order = []  # topological order
        visiting = set()
        visited = set()

        g = defaultdict(list)  # graph
        for p in prerequisites:
            g[p[0]].append(p[1])
            g[p[1]]  # ensures all vertices in graph

        for v in g:  # for vertex in graph
            dfs(v)

        return self.result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        ans = self.canFinish(numCourses, prerequisites)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
