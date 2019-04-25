class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(nums, rem):
            if rem == 0:
                result.add(tuple(sorted(nums)))
            for c in candidates:
                if rem >= c:
                    backtrack(nums+[c], rem-c)

        result = set()
        backtrack([], target)
        return list(result)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        candidates = [2, 3, 6, 7]
        target = 7
        ans = self.combinationSum(candidates, target)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
