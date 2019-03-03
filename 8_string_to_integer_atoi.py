class Solution(object):
    def myAtoi(self, str):
        max_int = 2147483647
        min_int = -2147483648
        bound = max_int

        result = 0
        sign = 1
        has_sign = False
        has_number = False

        plus_val = ord('+') - ord('0')
        minus_val = ord('-') - ord('0')
        whitespace_val = ord(' ') - ord('0')

        for i in range(len(str)):
            val = ord(str[i]) - ord('0')

            if not has_number:
                if not has_sign:
                    if val == whitespace_val:  # whitespace before sign and number
                        continue

            # assigns sign
            if not has_sign:
                if not has_number:
                    if (val == plus_val):
                        has_sign = True
                        continue
                    if (val == minus_val):
                        sign = -1
                        bound = min_int
                        has_sign = True
                        continue

            # assigns number
            if (val >= 0 and val <= 9):
                result = result * 10 + val
                has_number = True
            elif has_number:
                result = result * sign
                return result if abs(result) < abs(bound) else bound
            else:  # letter before number
                return 0

        result = result * sign
        return result if abs(result) < abs(bound) else bound

    def print_answer(self, ans):
        print(ans)

    def test(self):
        str = '   -42'
        ans = self.myAtoi(str)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
