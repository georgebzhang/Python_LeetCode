class Solution:
    # O(n^2) time
    # O(n) space
    def rob(self, nums):
        if not nums:
            return 0

        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]

        for i in range(1, N):
            dp[i] = nums[i]
            prev = i-1
            if prev > 0:
                dp[i] += max(dp[:prev])

        return max(dp)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [2, 7, 9, 3, 1]
        ans = self.rob(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
