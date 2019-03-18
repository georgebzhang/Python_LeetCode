class Solution(object):
    def removeElement(self, nums, val):
        while True:
            try:
                ind = nums.index(val)
                del nums[ind]
            except:
                return

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [3, 2, 2, 3]
        val = 3
        self.removeElement(nums, val)
        self.print_ans(nums)


if __name__ == '__main__':
    s = Solution()
    s.test()
