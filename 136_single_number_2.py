from collections import Counter


class Solution(object):
    def singleNumber(self, nums):
        c = Counter(nums)
        return min(c, key=lambda num: c[num])

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [2, 2, 1]
        ans = self.singleNumber(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
