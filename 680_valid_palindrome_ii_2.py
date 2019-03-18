class Solution(object):
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            t = s[i:j+1]
            return t == t[::-1]

        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)

        return True

    def print_ans(self, ans):
        print(ans)

    def test(self):
        s = 'abca'
        ans = self.validPalindrome(s)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
