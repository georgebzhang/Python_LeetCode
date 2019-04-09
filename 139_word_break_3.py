class Solution(object):
    def print_dp(self, dp):
        for row in dp:
            print(row)

    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for sublen in range(1, n+1):
            for i in range(0, n-sublen+1):  # i: start of substring
                substr = s[i:i+sublen]
                # print(substr)
                if substr in wordSet:
                    dp[i][i+sublen-1] = (1, -1)  # -1 indicates whole substring in wordSet
                    continue
                for j in range(i, i+sublen-1):  # j: split index of substring
                    if dp[i][j] and dp[j+1][i+sublen-1]:
                        dp[i][i+sublen-1] = (1, j)

        self.print_dp(dp)
        return not not dp[0][n-1]

    def print_ans(self, ans):
        print(ans)

    def test(self):
        s = "goalspecial"
        wordDict = ["go", "goal", "goals", "special"]
        ans = self.wordBreak(s, wordDict)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
