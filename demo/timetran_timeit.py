__author__ = 'Fang'

import time
import timeit


def str_time_to_second(str_time):
    tup_time = time.strptime(str_time.split(".")[0], "%Y-%m-%d %H:%M:%S")
    seconds = time.mktime(tup_time)
    return seconds


if __name__ == "__main__":
    # list deep copy f = d[:]
    # tim_sort is a sorting algorithm
    statement = "a=s[:]; tim_sort(a)"
    setup = \
        '''
        import random

        random.seed('fang')
        s = [random.random() for i in range(1000)]
        tim_sort = list.sort
        '''
    # The way timeit works is to run SETUP once and then make repeated calls to STATEMENT
    timer = timeit.Timer(statement, setup)
    # repeat to call STATEMENT 1000000 times
    print timer.timeit(1000000)
    # running STATEMENT 3 times and keeping only the best time
    # this can really help reduce measurement distortions due to other processes running on your system.
    print min(timer.repeat(3, 1000000))
