class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum_all = n*(n+1)//2
        sum_nums = 0
        for i in range(n):
            sum_nums += nums[i]
            
        return sum_all - sum_nums

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [3, 0, 1]
        ans = self.missingNumber(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
