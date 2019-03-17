def alter_list(l):
    l[1] = 69


if __name__ == '__main__':
    # l1 = [1, 2, 3]
    # l2 = [4, 5, 6]
    # l3 = [7, 8, 9]
    # l4 = [l1, l2, l3]
    # alter_list(l2)
    # print(l4)

    x = 69
    print('value:', x, 'id:', id(x))
    y = x
    print('value:', y, 'id:', id(y))
    y += 1
    print('value:', y, 'id:', id(y))

