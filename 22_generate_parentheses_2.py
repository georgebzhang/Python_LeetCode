class Solution:
    def generateParenthesis(self, n):
        def backtrack(s='', left=0, right=0):
            if len(s) == 2*n:
                result.append(s)
                return
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:  # this is the key observation
                backtrack(s+')', left, right+1)

        result = []
        backtrack()
        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        n = 3
        ans = self.generateParenthesis(n)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
