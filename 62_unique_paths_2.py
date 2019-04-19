from math import factorial


class Solution(object):
    def uniquePaths(self, m, n):
        def num_combinations(n, k):
            return int(factorial(n)/(factorial(k)*factorial(n-k)))

        steps = m-1 + n-1
        down_steps = m-1
        return num_combinations(steps, down_steps)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        m, n = 3, 2
        ans = self.uniquePaths(m, n)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
