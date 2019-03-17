class Solution(object):
    def kClosest(self, points, K):
        l_points = []
        for p in points:
            point = [p, p[0] ** 2 + p[1] ** 2]
            l_points.append(point)

        l_points_k = sorted(l_points, key=lambda point: point[1])[:K]
        result = [point[0] for point in l_points_k]
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
