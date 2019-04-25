class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(candidates, nums, rem):
            # print(nums)  # uncomment this to understand how backtrack works
            if rem == 0:
                result.append(nums)
            for i, cand in enumerate(candidates):
                if rem >= cand:
                    backtrack(candidates[i:], nums+[cand], rem-cand)  # candidates[i:] guarantees no duplicate lists in result

        candidates.sort()
        result = []
        backtrack(candidates, [], target)
        return result

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
