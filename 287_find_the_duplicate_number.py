class Solution(object):
    def findDuplicate(self, nums):
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return nums[i]
            else:
                s.add(nums[i])

        return -1

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [1, 3, 4, 2, 2]
        ans = self.findDuplicate(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
