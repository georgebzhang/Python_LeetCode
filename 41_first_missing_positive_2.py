class Solution(object):
    def firstMissingPositive(self, nums):
        s = set(nums)
        i, n = 1, len(s)
        while i <= n:
            if i not in s:
                return i
            i += 1
        return i if i == n+1 else 1

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 2, 0]
        ans = self.firstMissingPositive(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
