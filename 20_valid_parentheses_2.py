class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}

        stack = []
        for k in s:
            if k in mapping:
                if not stack or mapping[k] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(k)

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
