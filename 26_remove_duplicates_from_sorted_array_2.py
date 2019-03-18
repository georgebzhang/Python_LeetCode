class Solution(object):
    def removeDuplicates(self, nums):
        s = set(nums)
        nums[:] = sorted(list(s))

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 1, 2]
        self.removeDuplicates(nums)
        self.print_ans(nums)


if __name__ == '__main__':
    s = Solution()
    s.test()
