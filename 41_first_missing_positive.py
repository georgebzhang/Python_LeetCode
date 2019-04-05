from bisect import bisect_left


class Solution(object):
    def firstMissingPositive(self, nums):
        def index(num):
            ind = bisect_left(pos_nums, num)
            if ind != len(nums) and pos_nums[ind] == num:
                return ind
            raise ValueError

        pos_nums = [num for num in nums if num > 0]
        if not pos_nums:
            return 1
        pos_nums.sort()
        result = 1
        while True:
            try:
                index(result)
            except:
                return result
            result += 1

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 2, 0]
        ans = self.firstMissingPositive(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
