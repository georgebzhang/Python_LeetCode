class Solution(object):
    def wordBreak(self, s, wordDict):
        def wordBreakRec(s):
            if s in wordSet:
                return True
            for i in range(len(s)):
                s1 = s[:i+1]
                if s1 in wordSet:
                    s2 = s[i+1:]
                    if wordBreakRec(s2):
                        return True

            return False

        wordSet = set(wordDict)
        return wordBreakRec(s)

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
