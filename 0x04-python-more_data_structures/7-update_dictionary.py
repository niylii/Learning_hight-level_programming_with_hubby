#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    check = 0
    for k in a_dictionary:
        if key == k:
            a_dictionary[k] = value
            check = 1
    if check == 0:
        a_dictionary[key] = value
    return a_dictionary
