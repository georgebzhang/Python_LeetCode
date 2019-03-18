class Solution(object):
    # Top-Down Dynamic Programming
    def isMatch(self, s, p):
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = first_match and dp(i+1, j) or dp(i, j+2)  # if not first_match, dp(i+1, j) is short-circuited
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        memo = {}
        return dp(0, 0)

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
