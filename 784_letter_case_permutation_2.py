class Solution(object):
    def letterCasePermutation(self, S):
        def rec(perm, rem):
            if not rem:
                result.append(perm)
                return
            if rem[0].isalpha():
                rec(perm + rem[0].lower(), rem[1:])
                rec(perm + rem[0].upper(), rem[1:])
            else:
                rec(perm + rem[0], rem[1:])

        result = []
        rec('', S)
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
