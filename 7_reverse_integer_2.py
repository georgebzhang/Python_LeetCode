class Solution(object):
    def reverse(self, x):
        int_max = 2147483647
        int_min = -2147483648

        sign = 1 if x >= 0 else -1
        x = abs(x)

        x = str(x)
        x = x[::-1]
        x = sign * int(x)

        if x > int_max or x < int_min:
            return 0

        return x

    def print_answer(self, ans):
        print(ans)

    def test(self):
        x = 123
        ans = self.reverse(x)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
