class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []
        for k in s:
            if k in {'(', '{', '['}:
                stack.append(k)
            if k == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            if k == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            if k == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()

        return not stack

    def print_answer(self, ans):
        print(ans)

    def test(self):
        s = '()'
        ans = self.isValid(s)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
