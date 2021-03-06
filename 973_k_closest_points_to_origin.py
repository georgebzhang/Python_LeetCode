from math import sqrt
import heapq


class Solution(object):
    class Point(object):
        def __init__(self, c):  # c for coords
            self.c = c
            self.dist2 = c[0] ** 2 + c[1] ** 2

        def __lt__(self, other):
            return self.dist2 > other.dist2  # for max heap

    def kClosest(self, points, K):
        l_points = []
        for c in points:
            point = Solution.Point(c)
            l_points.append(point)

        l_points_k = l_points[:K]
        heapq.heapify(l_points_k)

        for i in range(K, len(l_points)):
            if not l_points[i] < l_points_k[0]:
                heapq.heappop(l_points_k)
                heapq.heappush(l_points_k, l_points[i])

        result = [point.c for point in l_points_k]
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
