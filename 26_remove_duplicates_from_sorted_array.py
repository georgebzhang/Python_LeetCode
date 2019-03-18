from collections import Counter


class Solution(object):
    def removeDuplicates(self, nums):
        c = Counter(nums)
        for k in c:
            for i in range(c[k] - 1):
                nums.remove(k)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 1, 2]
        self.removeDuplicates(nums)
        self.print_ans(nums)


if __name__ == '__main__':
    s = Solution()
    s.test()
