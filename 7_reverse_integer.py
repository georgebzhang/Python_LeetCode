class Solution(object):
    def reverse(self, x):
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        return rev

    def print_answer(self, ans):
        print(ans)

    def test(self):
        x = 123
        ans = self.reverse(x)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
