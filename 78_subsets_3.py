class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            temp = []
            for i in range(len(result)):
                comb = result[i]
                temp.append(comb + [num])
            result.extend(temp)

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [1, 2, 3]
        ans = self.subsets(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
