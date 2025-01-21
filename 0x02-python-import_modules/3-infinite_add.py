#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    sum_ = 0
    if argc == 0:
        print("0")
    else:
        for i in range(1, argc + 1):
            sum_ += int(sys.argv[i])
        print(f"{sum_}")
