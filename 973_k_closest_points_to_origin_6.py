from heapq import heapify, heappop, heappush, nsmallest


class Point(object):
    def __init__(self, c):  # c for coords
        self.c = c
        self.dist2 = c[0] ** 2 + c[1] ** 2


class Solution(object):

    def kClosest(self, points, K):
        l_points = []
        for c in points:
            l_points.append(Point(c))

        l_points_k = nsmallest(K, l_points, key=lambda point: point.dist2)

        return [point.c for point in l_points_k]

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
