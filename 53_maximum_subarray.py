class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        ans = self.maxSubArray(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
