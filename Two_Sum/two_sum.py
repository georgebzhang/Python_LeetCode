class Solution(object):
    def twoSum(self, nums, target):  # O(n)
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return [map[nums[i]], i]
            else:
                map[target - nums[i]] = i

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = self.twoSum(nums, target)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()

