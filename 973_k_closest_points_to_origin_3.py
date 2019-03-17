class Solution(object):
    def kClosest(self, points, K):
        # def distsq(coords):
        #     return coords[0] ** 2 + coords[1] ** 2
        #
        # return sorted(points, key=lambda c: distsq(c))[:K]
        return sorted(points, key=lambda c: c[0] ** 2 + c[1] ** 2)[:K]

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
