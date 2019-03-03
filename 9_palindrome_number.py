class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]

    def print_answer(self, ans):
        print(ans)

    def test(self):
        x = 121
        ans = self.isPalindrome(x)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
