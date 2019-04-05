class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            ind = abs(nums[i])-1
            nums[ind] = -abs(nums[ind])  # mark negative
        return [i+1 for i in range(n) if nums[i] > 0]

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        ans = self.findDisappearedNumbers(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
