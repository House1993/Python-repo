__author__ = 'Fang'

import random
import datetime


def func1(a):
    return a


def func2(a):
    return a


def gen_data():
    return random.random()


if __name__ == "__main__":
    num_iter = 100000000
    time1 = time2 = 0
    for i in xrange(num_iter):
        tst = gen_data()
        bgn = datetime.datetime.now()
        func1(tst)
        end1 = datetime.datetime.now()
        func2(tst)
        end2 = datetime.datetime.now()
        tmp = end1 - bgn
        time1 += tmp.days * 24 * 60 * 60 + tmp.seconds + tmp.microseconds / 1e6
        tmp = end2 - end1
        time2 += tmp.days * 24 * 60 * 60 + tmp.seconds + tmp.microseconds / 1e6
    print "func1 cost %s func2 cost %s\n" % (str(time1), str(time2))
