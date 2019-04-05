class Solution(object):
    def findWords(self, words):
        result = []
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        for word in words:
            word_lower = word.lower()
            word_set = set(word_lower)
            if word_set <= row1 or word_set <= row2 or word_set <= row3:
                result.append(word)

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        words = ["Hello", "Alaska", "Dad", "Peace"]
        ans = self.findWords(words)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
