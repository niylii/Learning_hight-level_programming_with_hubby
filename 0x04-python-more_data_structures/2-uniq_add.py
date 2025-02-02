#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    unique = set(my_list)
    for i in unique:
        num += i
    return num
