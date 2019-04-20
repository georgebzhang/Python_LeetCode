class Solution(object):
    def combine(self, n, k):
        def backtrack(num=1, comb=[]):
            if len(comb) == k:
                result.append(comb[:])

            for i in range(num, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()

        result = []
        backtrack()
        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        n, k = 4, 2
        ans = self.combine(n, k)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
