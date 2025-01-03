gen1 = [1, 2, 3, 4, 5]


def x123():
    for x1 in gen1:
        yield x1


if __name__ == '__main__':
    x1 = x123()
    print(tuple(x1))
