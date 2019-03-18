class Solution(object):
    def isMatch(self, s, p):
        # if not s: return not p  # base case
        # first_match = p[0] in {s[0], '.'}
        # return first_match and self.isMatch(s[1:], p[1:])

        # input('Enter your input:')
        # print(s)
        # print(p)

        if not p:
            return not s  # base case, can make expression below true with or self.isMatch(s, p[2:])

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            # isMatch(s, p[2:]) means first character repeated zero times
            return first_match and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])  # if not first_match, self.isMatch(s[1:], p) is short-circuited
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def print_answer(self, ans):
        print(ans)

    def test(self):
        s = 'aa'
        p = 'a*'
        ans = self.isMatch(s, p)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
