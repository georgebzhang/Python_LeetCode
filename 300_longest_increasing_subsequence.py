class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(0, i+1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])

        return max(dp)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        ans = self.lengthOfLIS(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
