"""
Insert a bunch of unique elements into a hash table (dict)
"""

import sys
import random

random.seed(0)

def main(size):
    """
    Insert |size| unique elements into |blah|
    """
    blah = {}
    for i in range(size):
        blah[i + (size * (random.randint(0, size)))] = i

if __name__ == '__main__':
    main(int(sys.argv[1]))
