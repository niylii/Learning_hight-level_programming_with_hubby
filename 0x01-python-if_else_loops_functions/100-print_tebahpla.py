#!/usr/bin/python3
for i in range(25, -1, -2):
    print(f"{chr(i + 97)}{chr(i - 1 + 65)}", end="")
    if i < 1:
        break
