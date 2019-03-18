class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        nums[:] = nums[:i+1]

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 1, 2]
        self.removeDuplicates(nums)
        self.print_ans(nums)


if __name__ == '__main__':
    s = Solution()
    s.test()
