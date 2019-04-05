class Solution(object):
    def singleNumber(self, nums):
        s = set()
        for num in nums:
            try:
                s.remove(num)
            except:
                s.add(num)
        return s.pop()

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [2, 2, 1]
        ans = self.singleNumber(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
