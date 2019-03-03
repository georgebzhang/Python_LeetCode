class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        orig = x
        reverse = 0
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return orig == reverse

    def print_answer(self, ans):
        print(ans)

    def test(self):
        x = 121
        ans = self.isPalindrome(x)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
