class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign_dividend = -1 if dividend < 0 else 1
        sign_divisor = -1 if divisor < 0 else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while True:
            dividend -= divisor
            if dividend >= 0:
                result += 1
            else:
                break

        return sign_dividend * sign_divisor * result

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
