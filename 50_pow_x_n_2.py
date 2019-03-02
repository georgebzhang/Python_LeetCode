class Solution(object):
    def pos_pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        ans = self.myPow(x, n // 2)
        ans *= ans
        if n % 2 == 1:
            ans *= x

        return ans

    def myPow(self, x, n):
        pos = True if n >= 0 else False
        pos_result = self.pos_pow(x, abs(n))
        return pos_result if pos else 1 / pos_result

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
