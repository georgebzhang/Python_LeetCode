# https://www.youtube.com/watch?v=lAXZGERcDf4
# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
from collections import defaultdict
from heapq import heapify, heappop
import sys


class Solution:
    def paths(self, parents, start):
        result = []
        for child in parents:
            path = [child]
            parent = parents[child]
            while True:
                path.append(parent)
                if parent == start:
                    break
                parent = parents[parent]
            result.append(path)

        return result

    def dijkstra(self, graph, start):
        distances = {v: sys.maxsize for v in graph}
        distances[start] = 0

        pq = []  # priority queue
        parents = {}

        for v, dist in distances.items():
            entry = [dist, v]
            pq.append(entry)
        heapify(pq)

        while pq:
            # dist1, v1 = heappop(pq)
            v1 = heappop(pq)[1]
            for v2, dist2 in graph[v1].items():
                dist = distances[v1] + dist2
                if dist < distances[v2]:
                    distances[v2] = dist
                    parents[v2] = v1

        return distances, parents

    def test(self):
        edge_list = [['A', 'B', 5], ['A', 'D', 9], ['A', 'E', 2],
                 ['B', 'C', 2],
                 ['C', 'D', 3],
                 ['D', 'F', 2],
                 ['E', 'F', 3]]

        graph = defaultdict(dict)
        for edge in edge_list:
            v1, v2, weight = edge
            graph[v1][v2] = weight
            graph[v2][v1] = weight
        # for k in graph:
        #     print(graph[k])

        distances, parents = self.dijkstra(graph, 'A')
        print(distances)
        # print(parents)
        paths = self.paths(parents, 'A')
        print(paths)


if __name__ == '__main__':
    s = Solution()
    s.test()
