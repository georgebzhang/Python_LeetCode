class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        result = []
        n = len(nums)
        s = set(nums)
        for i in range(1, n+1):
            if i not in s:
                result.append(i)

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        ans = self.findDisappearedNumbers(nums)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
