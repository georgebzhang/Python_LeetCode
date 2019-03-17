class Solution(object):
    def climbStairs(self, n):
        def rec(i):
            if i == 0 or i == 1:
                return 1
            return memo[i - 1] + memo[i - 2]

        memo = [0] * (n + 1)
        for i in range(n + 1):
            memo[i] = rec(i)

        return memo[n]

    def print_ans(self, ans):
        print(ans)

    def test(self):
        n = 2
        ans = self.climbStairs(n)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
