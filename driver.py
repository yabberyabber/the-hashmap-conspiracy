"""
Run a program that creates a map repeatedly with different
sizes and track the time it takes each round
"""

from subprocess import call
import timeit

print("%s, %s, %s, %s" % ("dataset size", "20th P", "50th P", "80th P"))
for size_power in [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]:
    times = []
    for i in range(9):
        size = int(10 ** size_power)

        start_time = timeit.default_timer()
        call(["./cpp/a.out", str(size)])
        elapsed = timeit.default_timer() - start_time

        times.append(elapsed)
    times = sorted(times)
    low, mid, high = times[2], times[4], times[6]
    print("%d, %f, %f, %f" % (size, low, mid, high))
