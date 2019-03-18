class Solution(object):
    # Bottom-Up Dynamic Programming
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)

        # memo[i][j] is True if s[i:] and p[j:] match
        memo = [[False] * (m+1) for _ in range(n+1)]
        memo[-1][-1] = True  # "base case": if both text and pattern

        # don't need to loop thru i from n-> 0 for j = m, since memo[n -> 0][m] = False, since pattern is depleted
        for i in range(n, -1, -1):  # i from n -> 0
            for j in range(m-1, -1, -1):  # j from m-1 -> 0
                first_match = i < n and p[j] in {s[i], '.'}
                if j+1 < m and p[j+1] == '*':
                    memo[i][j] = first_match and memo[i+1][j] or memo[i][j+2]
                else:
                    memo[i][j] = first_match and memo[i+1][j+1]

        return memo[0][0]

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
