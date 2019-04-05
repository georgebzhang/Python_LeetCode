class Solution(object):
    def trailingZeroes(self, n):
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n-1)

        n_fac = factorial(n)
        result = 0
        while n_fac > 0:
            if n_fac % 10 != 0:
                break
            result += 1
            n_fac //= 10
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
