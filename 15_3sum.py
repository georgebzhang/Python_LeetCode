class Solution(object):
    def threeSum(self, nums):
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if temp not in result:
                            result.append(temp)

        return result;

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [-1, 0, 1, 2, -1, -4]
        ans = self.threeSum(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
