class Solution(object):
    def two_sum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return [map[nums[i]], i]
            else:
                map[target - nums[i]] = i

    def test(self):
        nums = [2, 7, 11, 15]
        target = 9
        print(self.two_sum(nums, target))


if __name__ == '__main__':
    s = Solution()
    s.test()

