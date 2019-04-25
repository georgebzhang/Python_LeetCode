class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
                return 2 ** 31 - 1

        neg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        for i in range(32)[::-1]:
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                result |= (1 << i)

        return result if not neg else -result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        dividend = 10
        divisor = 3
        ans = self.divide(dividend, divisor)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
