"""
Track the number of writes per insertion into a hash table
assuming the capacity doubles and elements are re-inserted
when the table size/capacity exceeds the given load
factor
"""

MAX_LOAD = 1.0

def main():
    """
    Show a table for # writes per insert by # inserts
    """
    fmtstr = "| %4s | %8s | %8s | %12s | %20s |"

    print(fmtstr % ("size", "capacity", "# writes", "sum # writes", "writes / insert"))

    size = 1
    capacity = 1
    sum_writes = 1

    for _ in range(256):
        this_writes = 1
        if (size + 1) / capacity > MAX_LOAD:
            this_writes += capacity
            capacity = capacity * 2

        size += 1

        sum_writes += this_writes

        print(fmtstr % (
            str(size),
            str(capacity),
            str(this_writes),
            str(sum_writes),
            str(float(sum_writes) / float(size))))

if __name__ == '__main__':
    main()
