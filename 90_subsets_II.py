from collections import Counter


class Solution(object):
    def subsetsWithDup(self, nums):
        c = Counter(nums)
        result = [[]]
        for k in c:
            temp = []
            while result:
                l = result.pop()
                for i in range(c[k]+1):
                    temp.append(l + [k]*i)
            result = temp

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        nums = [1, 2, 3]
        ans = self.subsetsWithDup(nums)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
