from collections import deque


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


if __name__ == '__main__':
    l = [4, 2, 0, 8, 4]
    # print(get_2nd_min(l))
    # test(l)
    # print(l)
    # print(l[1], l[~1])
    # print(l[-1])
    # print(l[::])

    l = [1, 2, 3, 4, 5]
    dq = deque(l)
    for i in range(len(dq)):
        # print('{}, {}'.format(i, len(dq)))
        print(dq.pop())
