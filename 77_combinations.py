class Solution(object):
    def combine(self, n, k):
        nums = [_+1 for _ in range(n)]
        result = [[]]
        for num in nums:
            temp = []
            for i in range(len(result)):
                comb = result[i]
                temp.append(comb + [num])
            result.extend(temp)

        return [comb for comb in result if len(comb) == k]

    def print_answer(self, ans):
        print(ans)

    def test(self):
        n, k = 4, 2
        ans = self.combine(n, k)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
