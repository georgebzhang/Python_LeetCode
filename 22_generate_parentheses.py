class Solution:
    def generateParenthesis(self, n):
        def permute(perm, rem):
            if not rem:
                perms.add(perm[:])
            for i in range(len(rem)):
                permute(perm+rem[i], rem[:i]+rem[i+1:])

        def validParenthesis(s):
            mapping = {')': '('}
            stack = ''
            for k in s:
                if k in mapping:
                    if not stack or mapping[k] != stack[-1]:
                        return False
                    stack = stack[:-1]
                else:
                    stack += k

            return not stack

        perms = set()
        s = '('*n + ')'*n
        permute('', s)

        return [s for s in perms if validParenthesis(s)]

    def print_answer(self, ans):
        print(ans)

    def test(self):
        n = 3
        ans = self.generateParenthesis(n)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
