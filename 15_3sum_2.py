class Solution(object):
    def threeSum(self, nums):
        s = set()
        for i in range(len(nums) - 2):
            d = {}
            target = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] in d:
                    temp = [nums[i], nums[d[nums[j]]], nums[j]]
                    temp.sort()
                    s.add(tuple(temp))
                else:
                    d[target - nums[j]] = j

        return list(s)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [-1, 0, 1, 2, -1, -4]
        ans = self.threeSum(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
