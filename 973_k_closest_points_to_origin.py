from math import sqrt
import heapq


class Solution(object):
    class Point:
        def __init__(self, coords):
            self.coords = coords
            self.dist = sqrt(coords[0] ** 2 + coords[1] ** 2)

        def __lt__(self, other):
            return self.dist > other.dist  # for max heap
        
        def __str__(self):
            return '(coords: ' + str(self.coords) + ', dist: ' + str(self.dist) + ')'

    def kClosest(self, points, K):
        l_points = []
        for i in range(len(points)):
            p = Solution.Point(points[i])
            l_points.append(p)

        l_points_k = l_points[:K]  # max heap
        heapq.heapify(l_points_k)

        for i in range(K, len(l_points)):
            if not l_points[i] < l_points_k[0]:
                heapq.heappop(l_points_k)
                heapq.heappush(l_points_k, l_points[i])

        result = [p.coords for p in l_points_k]
        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        K = 2
        ans = self.kClosest(points, K)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
