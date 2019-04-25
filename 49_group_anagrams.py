from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs):
        mapping = defaultdict(list)
        for s in strs:
            mapping[tuple(sorted(Counter(s).elements()))].append(s)

        return list(mapping.values())

    def print_answer(self, ans):
        print(ans)

    def test(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        ans = self.groupAnagrams(strs)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
