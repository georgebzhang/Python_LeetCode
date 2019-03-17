class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1

        memo = [0] * (n+1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, n + 1):
            memo[i] = memo[i-1] + memo[i-2]

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
