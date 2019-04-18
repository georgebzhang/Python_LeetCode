# https://www.youtube.com/watch?v=oP2-8ysT3QQ
# https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/
from collections import defaultdict
from heapq import heapify, heappop, heappush


class Solution:
    def prim(self, graph):
        mst = defaultdict(set)
        vertices = [v for v in graph]
        v1 = vertices[0]
        visited = set(v1)
        edges = [(weight, v1, v2) for v2, weight in graph[v1].items()]  # priority queue
        heapify(edges)

        i = 1
        while edges:
            print('{}. visited: {}'.format(i, visited))
            print('{}. edges: {}'.format(i, edges))
            print('{}. mst: {}'.format(i, mst))
            weight, v1, v2 = heappop(edges)
            if v2 not in visited:
                visited.add(v2)
                mst[v1].add(v2)
                for v3, weight2 in graph[v2].items():
                    if v3 not in visited:
                        heappush(edges, (weight2, v2, v3))
            i += 1
        return mst

    def test(self):
        edge_list = [['A', 'B', 3], ['A', 'D', 1],
                 ['B', 'D', 3], ['B', 'C', 1],
                 ['C', 'D', 1], ['C', 'E', 5], ['C', 'F', 4],
                 ['D', 'E', 6],
                 ['E', 'F', 2]]

        graph = defaultdict(dict)
        for edge in edge_list:
            v1, v2, weight = edge
            graph[v1][v2] = weight
            graph[v2][v1] = weight
        # for k in graph:
        #     print(graph[k])

        mst = self.prim(graph)
        print(mst)


if __name__ == '__main__':
    s = Solution()
    s.test()
