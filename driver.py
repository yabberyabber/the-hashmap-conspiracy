"""
Run a program that creates a map repeatedly with different
sizes and track the time it takes each round
"""

from subprocess import call
import timeit
from collections import namedtuple
import statistics
from math import log
import numpy as np
import matplotlib.pyplot as plt

ResultRow = namedtuple("ResultRow", ["executable", "size", "low", "mid", "high"])

SIZES = list(np.arange(4.0, 7.5, 0.1))

def test_executable(name, execution_list):
    """
    Given a string path to an executable (which takes dataset size as first
    arg), test the dataset with varying sizes of datasets and record
    the performance over several trials.
    """
    ret = []
    print("Testing: %s" % (name,))
    print("%s, %s, %s, %s" % ("dataset size", "x-SD", "mean", "x+SD"))
    for size_power in SIZES:
        times = []
        for _ in range(15):
            size = int(10 ** size_power)

            subst_exe_list = [
                str(size) if x == '$SIZE' else x
                for x
                in execution_list]

            start_time = timeit.default_timer()
            call(subst_exe_list)
            elapsed = timeit.default_timer() - start_time

            times.append(elapsed)
        mean = statistics.mean(times)
        stdev = statistics.stdev(times)

        low, mid, high = mean - stdev, mean, mean + stdev
        ret.append(ResultRow(
            name, size, low, mid, high))
        print("%d, %f, %f, %f" % (size, low, mid, high))
    return ret

def render_plot(name, data):
    """
    Given a list of |ResultRow| entries, render a plot as a .png
    The x axis should be the log base 10 of the dataset size
    The y axis should be the time per insertion
    """
    for row in data:
        x_val = log(row.size, 10)
        y_low = row.low / row.size
        y_med = row.mid / row.size
        y_high = row.high / row.size

        plt.plot([x_val, x_val, x_val], [y_low, y_med, y_high], "ro")

    ticks = [size for size in SIZES if str(size)[-1] in ['0', '5']]

    plt.xticks(ticks, ["10^" + str(tick) for tick in ticks])
    plt.xlabel("Number of Insertions (log scale)")
    plt.ylabel("Time per Insertion (seconds)")
    plt.tight_layout()
    plt.savefig(name)
    plt.close()

def main():
    """
    Run trials on all known implementations and save all their graphs locally
    """
    implementations = {
        'cpp': ['cpp/Main', '$SIZE'],
        'java': ['java', 'java_hashmap/Main', '$SIZE'],
        'python': ['python', 'py/main.py', '$SIZE'],
        'go': ['go/main', '$SIZE'],
        'rust': ['rust/target/release/rust', '$SIZE'],
    }

    for implementation, execution_list in implementations.items():
        data = test_executable(implementation, execution_list)
        render_plot(implementation + '.png', data)

if __name__ == '__main__':
    main()
