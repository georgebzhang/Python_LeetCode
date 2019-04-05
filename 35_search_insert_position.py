from bisect import bisect_left as bsl


class Solution(object):
    def searchInsert(self, nums, target):
        return bsl(nums, target)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 3, 5, 6]
        target = 5
        ans = self.searchInsert(nums, target)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
