class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        num_intervals = len(intervals)
        if num_intervals == 1:  # not needed
            return intervals

        intervals.sort(key=lambda interval: interval.start)
        result = []
        current = intervals[0]
        for i in range(1, num_intervals):
            interval = intervals[i]
            if interval.start > current.end:  # no overlap
                result.append(current)
                current = interval
            else:
                current.end = max(current.end, interval.end)

        result.append(current)  # append last interval, also handles len(intervals) == 1
        return result

    def print_answer(self, ans):
        print('[', end='')
        for i in range(len(ans)):
            interval = ans[i]
            print('[{}, {}]'.format(interval.start, interval.end), end='')
            if i != len(ans) - 1:
                print(', ', end='')
        print(']')

    def test(self):
        input = [[1, 3], [2, 6], [8, 10], [15, 18]]
        intervals = []
        for s, e in input:
            interval = Interval(s, e)
            intervals.append(interval)
        ans = self.merge(intervals)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
