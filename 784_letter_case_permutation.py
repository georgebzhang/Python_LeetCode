class Solution(object):
    def letterCasePermutation(self, S):
        result = ['']
        for k in S:
            temp = []
            while result:
                perm = result.pop()
                if k.isalpha():
                    temp.append(perm + k.lower())
                    temp.append(perm + k.upper())
                else:
                    temp.append(perm + k)
            result = temp

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        S = 'a1b2'
        ans = self.letterCasePermutation(S)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
