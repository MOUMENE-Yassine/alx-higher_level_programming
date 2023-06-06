#!/usr/bin/python3
def uppercase(str):
    n = ord('A') - ord('a')
    for c in str:
        c = chr(n + ord(c)) if 97 <= ord(c) <= 122 else c
        print("{}".format(c), end="")
    print()
