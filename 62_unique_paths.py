class Solution(object):
    def uniquePaths(self, m, n):
        dirs = ((1, 0), (0, 1))
        def neighbors(p):
            i0, j0 = p
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                if 0 <= i < n and 0 <= j < m:
                    result.append((i, j))
            return result

        def paths(p):
            if p == end:
                return [[p]]
            result = []
            for n in neighbors(p):
                for path in paths(n):
                    result.append([p] + path)
            return result

        start, end = (0, 0), (n-1, m-1)
        return len(paths(start))

    def print_ans(self, ans):
        print(ans)

    def test(self):
        m, n = 3, 2
        ans = self.uniquePaths(m, n)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
