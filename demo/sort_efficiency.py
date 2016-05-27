__author__ = "House"


# sort demo. node(x, y) sorted by decrease y and increase x
# define a cmp func to decide who is smaller between 2 objects
def d(a, b):
    if a[1] != b[1]:
        if a[1] > b[1]:
            return 1
        else:
            return -1
    else:
        if a[0] < b[0]:
            return 1
        elif a[0] > b[0]:
            return -1
        else:
            return 0


if __name__ == "__main__":
    f = [(1, 2), (2, 2), (3, 2), (1, 3), (3, 3), (2, 3), (3, 1), (1, 1), (2, 1), (3, 2)]
    # for python 2.x, cmp can be use.
    print sorted(f, cmp=d, reverse=True)
    print f
    # for python 3.x, wo can only use key
    # using key is faster than using cmp
    print sorted(f, key=lambda x: (-x[1], x[0]))
    print f
