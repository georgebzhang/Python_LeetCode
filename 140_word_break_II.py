class Solution(object):
    def print_dp(self, dp):
        for row in dp:
            print(row)

    def wordBreak(self, s, wordDict):
        def dfs(p):
            i, j = p
            substr = s[i:] if j == -1 else s[i:j+1]
            if substr not in wordSet:
                return
            path.append(j)
            if j == -1:
                paths.append(path.copy())
                path.pop()
                return

            i = j+1
            for j in dp[j+1][-1]:
                p = (i, j)
                dfs(p)
            path.pop()

        wordSet = set(wordDict)
        n = len(s)
        dp = [[[] for _ in range(n)] for _ in range(n)]

        for sublen in range(1, n+1):
            for i in range(0, n-sublen+1):  # i: start of substring
                substr = s[i:i+sublen]
                if substr in wordSet:
                    dp[i][i+sublen-1].append(-1)  # -1 indicates whole substring in wordSet
                for j in range(i, i+sublen-1):  # j: split index of substring
                    if dp[i][j] and dp[j+1][i+sublen-1]:
                        dp[i][i+sublen-1].append(j)

        # self.print_dp(dp)

        paths = []
        i = 0
        for j in dp[0][n-1]:
            p = (i, j)
            path = []
            dfs(p)

        result = []
        for p in paths:
            i = 0
            words = []
            for j in p:
                if j == -1:
                    words.append(s[i:])
                    break
                words.append(s[i:j+1])
                words.append(' ')
                i = j+1
            result.append(''.join(words))

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        ans = self.wordBreak(s, wordDict)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
