from collections import deque
from collections import Counter, defaultdict


# def get_2nd_min(l):
#     min1 = get_min(l)
#     l.remove(min1)
#     return get_min(l)
#
# def get_min(l):
#     result = l[0]
#     for num in l:
#         if result > num:
#             result = num
#     return result

def test(l):
    l[0] = 69


def f():
    global s
    print(s)
    s = 'changed'
    print(s)


if __name__ == '__main__':
    # l = [4, 2, 0, 8, 4]
    # # print(get_2nd_min(l))
    # # test(l)
    # # print(l)
    # # print(l[1], l[~1])
    # # print(l[-1])
    # # print(l[::])
    #
    # l = [1, 2, 3, 4, 5]
    # dq = deque(l)
    # for i in range(len(dq)):
    #     # print('{}, {}'.format(i, len(dq)))
    #     print(dq.pop())
    # s = 'hi'
    # f()
    # print(s)
    # l = [1, 1, 1, 2, 2, 3, 4, 4]
    # c = Counter(l)
    # print(min(c, key=lambda k: c[k]))
    #
    # hi = (3, 3)
    # print(type(hi))
    #
    # lol = 3
    # lol += 1 if False else 0
    # print(lol)
    #
    # d = defaultdict(lambda: False)
    # d['hey'] = True
    # print(d['hi'])
    # # print(d['hey'])
    #
    s = 'abcde'
    print(s[~0])

    # s = 'a'
    # print('hi')
    # print(s[1:])
    # print('hi')

    q = deque([5])
    print(q)
    p = deque()
    p.append(3)
    print(p)