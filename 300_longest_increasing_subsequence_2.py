from bisect import bisect_left as bsl


class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [0]*n
        result = 0
        for num in nums:
            i = bsl(dp, num, 0, result)
            dp[i] = num
            if i == result:
                result += 1

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        ans = self.lengthOfLIS(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
