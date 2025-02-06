#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    prev = 0
    if roman_string is None:
        return 0
    for i in roman_string[::-1]:
        curr = romans[i]
        if curr < prev:
            number -= curr
        else:
            number += curr
        prev = curr
    return number
