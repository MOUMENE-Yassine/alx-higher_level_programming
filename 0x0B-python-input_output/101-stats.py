#!/usr/bin/python3
"""Reads from standard input and computes metrics module"""


def print_stats(n, status_codes):
    """Print accumulated metrics"""

    print("File size: {}".format(n))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))


if __name__ == "__main__":
    from sys import stdin

    n = 0
    status_codes = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    x = 0

    try:
        for line in stdin:
            if x == 10:
                print_stats(n, status_codes)
                x = 1
            else:
                x += 1

            line = line.split()

            try:
                n += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(n, status_codes)

    except KeyboardInterrupt:
        print_stats(n, status_codes)
        raise
