class Solution(object):
    def singleNumber(self, nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [2, 2, 1]
        ans = self.singleNumber(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
