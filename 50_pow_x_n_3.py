class Solution(object):
    def myPow(self, x, n):
        def pos_pow(x, n):
            if n == 0:  # base case
                return 1

            odd = n % 2 == 1
            m = n // 2

            xm = self.myPow(x, m)
            result = xm * xm
            if odd:
                result *= x

            return result

        neg = n < 0
        result = pos_pow(x, abs(n))
        if neg:
            result = 1 / result

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        x = 2
        n = 10
        ans = self.myPow(x, n)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
