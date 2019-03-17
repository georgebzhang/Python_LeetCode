class Solution(object):
    class Point(object):
        def __init__(self, c):  # c for coords
            self.c = c
            self.dist2 = c[0]**2 + c[1]**2

    def kClosest(self, points, K):
        l_points = []
        for c in points:
            point = Solution.Point(c)
            l_points.append(point)

        result = sorted(l_points, key=lambda point: point.dist2)[:K]
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
