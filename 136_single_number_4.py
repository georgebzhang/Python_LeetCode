class Solution(object):
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [2, 2, 1]
        ans = self.singleNumber(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
