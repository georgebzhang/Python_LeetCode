class Solution(object):
    def trailingZeroes(self, n):
        result = 0
        i = 5
        while i <= n:
            result += n // i
            i *= 5

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        n = 10
        ans = self.trailingZeroes(n)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
