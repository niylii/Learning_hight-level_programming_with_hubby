#!/usr/bin/python3
for i in range(0, 89):
    j = i + 1
    for j in range(1, 10):
        if i == j or i > j:
            continue
        elif i < 8:
            print(f"{i}{j}", end=", ")
    if i == 8:
        print(f"89")
